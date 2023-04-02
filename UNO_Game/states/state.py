#베이스 클래스. 즉 다른 클래스들이 상속받는 클래스
#State는 Scene과 함께 동작하며, 게임의 상태를 나타냅니다. 
#각각의 Scene은 특정한 State에 대응되며, 각 State는 게임에서 어떤 동작을 수행하는지 정의합니다. 
#예를 들어, 게임 시작 화면(Scene)에서는 '게임 시작', '설정', '종료' 버튼을 누르는 등의 동작이 가능합니다. 이러한 동작들은 각각 다른 State에 대응됩니다.
class State:
    def __init__(self):
        self.next_state = None
        self.quit = False

    def startup(self):
        pass

    def cleanup(self):
        pass

    def update(self, surface, keys):
        pass

    def draw(self, surface):
        pass

    def get_event(self, event):
        pass

    
    

# 각각의 화면 상태 클래스들은 State 클래스를 상속받아 구현되어야 합니다. 이 클래스는 이벤트 핸들링, 상태 업데이트, 화면 렌더링을 담당하는 메소드를 정의합니다.