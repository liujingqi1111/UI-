from nicegui import ui
import random

class GuessNumberGame:
    def __init__(self):
        self.target_number = random.randint(1, 100)
        self.init_ui()

    def init_ui(self):
        with ui.column().style('align-items: center; justify-content: center; height: 100vh; text-align: center;'):
            ui.label('猜数游戏').style('font-size: 36px; font-weight: bold;')
            self.label = ui.label('请输入一个1到100之间的数字：').style('font-size: 24px; margin-top: 20px;')
            self.input = ui.input().style('font-size: 24px; width: 200px; margin-top: 20px;')
            self.result_label = ui.label('').style('font-size: 24px; margin-top: 20px;')
            ui.button('提交', on_click=self.check_guess).style(
                'font-size: 24px; background-color: lightblue; margin-top: 20px; width: 100px;')
            ui.label('auther: Xidian ljq').style('font-size: 18px; margin-top: 40px; color: grey;')

    def check_guess(self):
        try:
            guess = int(self.input.value)
        except ValueError:
            self.result_label.text = '请输入一个有效的整数！'
            self.result_label.style('color: red;')
            return
        if guess < 1 or guess > 100:
            self.result_label.text = '请输入1到100之间的数字！'
            self.result_label.style('color: red;')
        elif guess < self.target_number:
            self.result_label.text = '猜小了！'
            self.result_label.style('color: orange;')
        elif guess > self.target_number:
            self.result_label.text = '猜大了！'
            self.result_label.style('color: red;')
        else:
            self.result_label.text = '恭喜你，猜对了！'
            self.result_label.style('color: green;')
            # 重置游戏
            self.target_number = random.randint(1, 100)
            self.label.text = '游戏重新开始，请输入一个1到100之间的数字：'
            self.input.value = ''

if __name__ in {"__main__", "__mp_main__"}:
    game = GuessNumberGame()
    ui.run()




