import os

class ScriptReader:
    def read_test_script(self,test_script_file: str) -> list:
        new_input_lines = []
        if not os.path.exists(test_script_file):
            print("파일을 찾을 수 없습니다.")
            return new_input_lines

        f = open(test_script_file, encoding='utf-8')
        for _ in range(500):
            input_line = f.readline()
            if self.is_valid_input(input_line):
                new_input_lines.append(input_line.strip())

        return new_input_lines

    def is_valid_input(self,input_line: str) -> bool:
        if len(input_line.strip().split()) == 2:
            return True
        return False