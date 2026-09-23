import logging

from .serializers import UserSerializer
from rest_framework import generics


from .models import User

logger_views_users = logging.getLogger(__name__)
file_handler = logging.FileHandler(f"log/{__name__}.log", mode="a", encoding="UTF8")
file_formatter = logging.Formatter(
    "\n%(asctime)s %(levelname)s %(name)s \n%(funcName)s %(lineno)d: \n%(message)s",
    datefmt="%H:%M:%S %d-%m-%Y",
)
file_handler.setFormatter(file_formatter)
logger_views_users.addHandler(file_handler)
logger_views_users.setLevel(logging.INFO)


# API
class UsersAPI(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
