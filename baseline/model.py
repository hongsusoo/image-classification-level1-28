import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.models as models
from efficientnet_pytorch import EfficientNet


class EfficientNetB6(nn.Module):
    def __init__(self, num_classes):
        super().__init__()
        self.backbone = EfficientNet.from_pretrained(
            "efficientnet-b6", num_classes)

    def forward(self, x):
        return self.backbone(x)


class EfficientNetB7(nn.Module):
    def __init__(self, num_classes):
        super().__init__()
        self.backbone = EfficientNet.from_pretrained(
            "efficientnet-b7", num_classes)

    def forward(self, x):
        return self.backbone(x)


class imgInceptionV3(nn.Module): #input size : (299,299)
    def __init__(self, num_classes):
        super(imgInceptionV3, self).__init__()
        self.model = models.inception_v3(pretrained=True, aux_logits = False)
        # self.inception_v3.fc = nn.Linear(2048, num_classes)
        self.num_classes=num_classes
    def forward(self, x):
        x = self.model(x)
        return x
            
        
class denseNet(nn.Module): #input size : (224,224)
    def __init__(self, num_classes):
        super(denseNet, self).__init__()
        self.model = models.densenet161(pretrained=True)
        # self.densenet.classifier = nn.Linear(2208, 18)
        self.num_classes=num_classes
    def forward(self, x):
        x = self.model(x)
        return x


class BaseModel(nn.Module):
    def __init__(self, num_classes):
        super().__init__()

        self.conv1 = nn.Conv2d(3, 32, kernel_size=7, stride=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, stride=1)
        self.conv3 = nn.Conv2d(64, 128, kernel_size=3, stride=1)
        self.dropout1 = nn.Dropout(0.25)
        self.dropout2 = nn.Dropout(0.25)
        self.avgpool = nn.AdaptiveAvgPool2d((1, 1))
        self.fc = nn.Linear(128, num_classes)

    def forward(self, x):
        x = self.conv1(x)
        x = F.relu(x)

        x = self.conv2(x)
        x = F.relu(x)
        x = F.max_pool2d(x, 2)
        x = self.dropout1(x)

        x = self.conv3(x)
        x = F.relu(x)
        x = F.max_pool2d(x, 2)
        x = self.dropout2(x)

        x = self.avgpool(x)
        x = x.view(-1, 128)
        return self.fc(x)


# Custom Model Template
class MyModel(nn.Module):
    def __init__(self, num_classes):
        super().__init__()

        """
        1. 위와 같이 생성자의 parameter 에 num_claases 를 포함해주세요.
        2. 나만의 모델 아키텍쳐를 디자인 해봅니다.
        3. 모델의 output_dimension 은 num_classes 로 설정해주세요.
        """

    def forward(self, x):
        """
        1. 위에서 정의한 모델 아키텍쳐를 forward propagation 을 진행해주세요
        2. 결과로 나온 output 을 return 해주세요
        """
        return x
