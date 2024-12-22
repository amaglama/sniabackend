from backend_mmaya.permissions import IsInGroup, IsSectorUser
from logs.models import UserAction
from .models import* 
from .serializers import *
from authentication.models import UserMenu,CustomUser,Menu,GroupMenu
from authentication.serializers import UserSerializer
from backend_mmaya.views import SoftDeleteModelViewSet
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import generics,permissions, filters, viewsets, status
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from django.db.models import Prefetch, Q
class AuthPermissionViewSet(SoftDeleteModelViewSet):
    queryset = AuthPermission.objects.all()
    serializer_class = AuthPermissionSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']

class AuthGroupViewSet(SoftDeleteModelViewSet):
    queryset = AuthGroup.objects.all()
    serializer_class = AuthGroupSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']

#---------------------------------------------------------------------------
from django.db.models import Q
class UserListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.filter(is_active=True, is_deleted=False).prefetch_related(
        Prefetch('menus', queryset=Menu.objects.filter(is_deleted=False))
    )
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AuthUserSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.query_params.get('search')

        if search:
            queryset = queryset.filter(
                Q(username__icontains=search) |
                Q(first_name__icontains=search) |
                Q(last_name__icontains=search) |
                Q(groups__name__icontains=search)
            ).distinct()

        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def perform_create(self, serializer):
        validated_data = serializer.validated_data
        group_id = validated_data.pop('group')
        menus_ids = validated_data.pop('menus')
        permissions_ids = validated_data.pop('permissions')
        #cargo_id = validated_data.pop('cargo')

        group = AuthGroup.objects.get(id=group_id.id)
        menus_group = group.menus.all()
        permissions_group = group.permissions.all()

        menus = Menu.objects.filter(id__in=[menu.id for menu in menus_ids])
        permissions = AuthPermission.objects.filter(id__in=[perm.id for perm in permissions_ids])

        combined_menus = list(set(menus) | set(menus_group))

        combined_permissions = list(set(permissions) | set(permissions_group))

        password = validated_data.pop('password', None)
        
        if password is not None:
            validated_data['password'] = make_password(password)
        #user = serializer.save(cargo=cargo_id)
        user = serializer.save()
        user.groups.add(group)
        user.menus.set(combined_menus)
        user.permissions.set(combined_permissions)
        
class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.filter(is_active=True, is_deleted=False)
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UpdateAuthUserSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        ##instance = CustomUser.objects.prefetch_related('groups','menus', 'permissions').get(pk=instance.pk)
        serializer = AuthUserSerializer(instance)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_deleted = True
        instance.is_active = False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ContentTypeView(viewsets.ModelViewSet):
    queryset = DjangoContentType.objects.all()
    serializer_class = DjandoContentTypeSerializer
    permission_classes = [permissions.IsAuthenticated]

class AuthUserUserPermissionsViewSet(viewsets.ModelViewSet):
    queryset = AuthUserUserPermissions.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return AuthUserUserPermissionsCreateSerializer
        return AuthUserUserPermissionsReadSerializer

class AuthGroupPermissionsViewSet(viewsets.ModelViewSet):
    queryset = AuthGroupPermissions.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return AuthGroupPermissionsCreateSerializer
        return AuthGroupPermissionsReadSerializer

class AuthUserGroupsViewSet(viewsets.ModelViewSet):
    queryset = AuthUserGroups.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return AuthUserGroupsCreateSerializer
        return AuthUserGroupsReadSerializer

class UserMenuViewSet(viewsets.ModelViewSet):
    queryset = UserMenu.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return UserMenuCreateSerializer
        return UserMenuReadSerializer
# class ProgramaViewSet(SoftDeleteModelViewSet):
#     queryset = Programa.objects.filter(is_deleted=False)
#     serializer_class = ProgramaSerializer
#     permission_classes = [permissions.AllowAny]

class GroupMenuViewSet(viewsets.ModelViewSet):
    queryset = GroupMenu.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create':
            return GroupMenuCreateSerializer
        return GroupMenuSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        group = serializer.validated_data['group']
        menus = serializer.validated_data['menu']
        
        group_menus = []
        for menu in menus:
            group_menu = GroupMenu(group=group, menu=menu)
            group_menus.append(group_menu)

        GroupMenu.objects.bulk_create(group_menus)
        
        return Response({'status': 'success'}, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['delete'])
    def delete_menus(self, request, *args, **kwargs):
        group_id = request.data.get('group_id')
        menu_ids = request.data.get('menu_ids')

        if not group_id or not menu_ids:
            return Response({'error': 'group_id and menu_ids are required.'}, status=status.HTTP_400_BAD_REQUEST)

        GroupMenu.objects.filter(group_id=group_id, menu_id__in=menu_ids).delete()

        return Response({'status': 'success'}, status=status.HTTP_204_NO_CONTENT)
