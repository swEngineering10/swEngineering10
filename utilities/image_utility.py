import os
import pygame
 
#  pygame 라이브러리를 사용하여 이미지를 로드하는 함수
def load_image(name: str, colorkey: int = None, directory: str = '../assets'): # name: 로드할 이미지의 이름, colorkey: 이 값을 설정하면 이미지에서 해당 색상을 지우고 투명한 배경으로 만듭니다. 기본값은 None입니다. directory: 이미지 파일이 저장된 디렉토리의 경로입니다. 기본값은 '../assets'입니다.
    fullname = os.path.join(directory, name) # 파일 경로를 조합하여 fullname 변수에 할당
    if not os.path.isfile(fullname): #  해당 파일이 존재하는지 확인하고, 없으면 예외를 발생시킵니다.
        raise FileNotFoundError(f"이미지 파일 '{fullname}' 를 찾을 수 없음")
    image = pygame.image.load(fullname) # 이미지를 로드한 후, colorkey 매개 변수가 설정되어 있다면, 이미지의 배경을 지정된 색상으로 바꿉니다. -1 값이 colorkey로 전달되면, 이미지의 좌측 상단 픽셀 색상을 사용합니다. 그렇지 않으면 전달된 색상을 사용합니다.
    if colorkey is not None: # colorkey가 설정되어 있지 않으면, 이미지를 투명 배경을 갖는 알파 채널을 포함한 포맷으로 변환합니다. 그런 다음 이미지를 반환합니다.
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image
