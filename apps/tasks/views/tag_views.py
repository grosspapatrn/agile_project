from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from apps.tasks.models.tag import Tag
from apps.tasks.serializers.tag_serializers import TagSerializer


class TagListAPIView(APIView):
    def get_objects(self) -> Tag:
        return Tag.objects.all()

    def get(self, request: Request) -> Response:
        tags = self.get_objects()

        if not tags.exists():
            return Response(
                data=[],
                status=status.HTTP_204_NO_CONTENT
            )

        serializer = TagSerializer(tags, many=True)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )