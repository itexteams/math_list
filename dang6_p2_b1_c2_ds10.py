import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang6_p2_b1_c2_ds10(self):
                # Khai báo biến (Random hệ số và Random dấu bất phương trình)
                x, y = symbols('x y')
                a = randint(2, 5)
                b = randint(2, 5)
                c = randint(4, 9)
                
                # Random dấu bất phương trình
                signs = ['\\le', '<', '\\ge', '>']
                chosen_sign = random.choice(signs)
                
                # ==================== XỬ LÝ ĐỒ THỊ TIKZ THEO PHONG CÁCH MỚI ====================
                # Khung tọa độ clipping
                x_min, x_max = -4, 6
                y_min, y_max = -4, 6
                
                # Tính tọa độ y của đường thẳng ax + by = c tại 2 biên x_min và x_max
                y_left = round((c - a * x_min) / b, 2)
                y_right = round((c - a * x_max) / b, 2)
                
                # Nét liền hay nét đứt tùy theo dấu bất phương trình
                if chosen_sign in ['\\le', '\\ge']:
                    line_style = "black"
                    border_status = "bao gồm cả bờ"
                else:
                    line_style = "black, dashed"
                    border_status = "không bao gồm bờ"
                
                # Xác định miền nghiệm (tô màu trắng fill[white]), miền còn lại gạch sọc đen
                if chosen_sign in ['\\le', '<']:
                    # Miền nghiệm chứa O(0,0) -> Nửa mặt phẳng phía dưới đường thẳng tô trắng
                    fill_white = f"\\fill[white] ({x_min},{y_left}) -- ({x_max},{y_right}) -- ({x_max},{y_min}) -- ({x_min},{y_min}) -- cycle;"
                else:
                    # Miền nghiệm không chứa O(0,0) -> Nửa mặt phẳng phía trên đường thẳng tô trắng
                    fill_white = f"\\fill[white] ({x_min},{y_left}) -- ({x_max},{y_right}) -- ({x_max},{y_max}) -- ({x_min},{y_max}) -- cycle;"
                
                # Tách riêng phần câu hỏi (chỉ gồm chữ)
                noidungcauhoi = f'Cho bất phương trình bậc nhất hai ẩn ${a}x + {b}y {chosen_sign} {c}$. Khi đó các mệnh đề sau đúng hay sai?'
                
                # Mã TikZ hình vẽ theo phong cách gạch sọc miền bỏ / miền nghiệm màu trắng
                hinh_ve_tikz = (f'''\\begin{{center}}
\\begin{{tikzpicture}}[>=stealth, scale=0.5, line width=1pt]
\\clip ({x_min},{y_min}) rectangle ({x_max},{y_max});
\\fill[pattern=north east lines, pattern color=black] ({x_min},{y_min}) rectangle ({x_max},{y_max});
{fill_white}
\\draw[->] ({x_min},0) -- ({x_max},0) node[below] {{$x$}};
\\draw[->] (0,{y_min}) -- (0,{y_max}) node[left] {{$y$}};
\\node at (0,0) [below left] {{$O$}};
\\draw[{line_style}] ({x_min},{y_left}) -- ({x_max},{y_right});
\\end{{tikzpicture}}
\\end{{center}}''')
                
                ######################################################################## Xử lý Tọa độ Đúng/Sai theo dấu ############################
                if chosen_sign in ['\\le', '<']:
                    pt_nb_true, pt_nb_false = (0, 0), (c, c)
                    pt_th_true, pt_th_false = (-c, 1), (c, 1)
                else:
                    pt_nb_true, pt_nb_false = (c, c), (0, 0)
                    pt_th_true, pt_th_false = (c, 1), (-c, 1)
                
                ######################################################################## Nhận biết ############################################
                nb_da_1_d = f'\\True Cặp $({pt_nb_true[0]};{pt_nb_true[1]})$ là một nghiệm của bất phương trình'
                nb_da_1_s = f'Cặp $({pt_nb_false[0]};{pt_nb_false[1]})$ là một nghiệm của bất phương trình'
                list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
                
                ######################################################################## Thông hiểu ############################################
                th_da_1_d = f'\\True Điểm $B({pt_th_true[0]};{pt_th_true[1]})$ thuộc miền nghiệm của bất phương trình đã cho'
                th_da_1_s = f'Điểm $B({pt_th_false[0]};{pt_th_false[1]})$ thuộc miền nghiệm của bất phương trình đã cho'
                list_th_da_1 = [th_da_1_d, th_da_1_s]
                
                ######################################################################## Vận dụng ############################################
                vd_da_1_d = '\\True Với $x = 0$ thì có vô số giá trị của $y$ thỏa mãn bất phương trình'
                vd_da_1_s = 'Với $x = 0$ thì chỉ có $2$ giá trị của $y$ thỏa mãn bất phương trình'
                list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
                
                ######################################################################## Vận dụng cao ############################################
                if chosen_sign in ['\\le', '\\ge']:
                    vdc_da_1_d = f'\\True Miền nghiệm của bất phương trình đã cho là miền không bị gạch sọc trong hình vẽ bao gồm cả bờ'
                    vdc_da_1_s = f'Miền nghiệm của bất phương trình đã cho là miền không bị gạch sọc trong hình vẽ không bao gồm bờ'
                else:
                    vdc_da_1_d = f'\\True Miền nghiệm của bất phương trình đã cho là miền không bị gạch sọc trong hình vẽ không bao gồm bờ'
                    vdc_da_1_s = f'Miền nghiệm của bất phương trình đã cho là miền không bị gạch sọc trong hình vẽ bao gồm cả bờ'
                list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
                
                def count_true_answers(answers):
                    return sum('\\True' in ans for ans in answers)
                
                # Lặp đến khi đáp án có từ 1 đến 3 đúng
                while True:
                    nb_da_1 = random.choice(list_nb_da_1)
                    th_da_1 = random.choice(list_th_da_1)
                    vd_da_1 = random.choice(list_vd_da_1)
                    vdc_da_1 = random.choice(list_vdc_da_1)
                    answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                    true_count = count_true_answers(answers)
                    if 1 <= true_count <= 3:
                        break
                
                ######################################################################## Xử lý Lời giải tự động ############################
                if nb_da_1 == nb_da_1_d:
                    val = a*pt_nb_true[0] + b*pt_nb_true[1]
                    loigiai_nb_1 = f'Thay $x={pt_nb_true[0]}; y={pt_nb_true[1]}$ vào bất phương trình ta được ${val} {chosen_sign} {c}$ (thỏa mãn). Vậy mệnh đề đúng.'
                else:
                    val = a*pt_nb_false[0] + b*pt_nb_false[1]
                    loigiai_nb_1 = f'Thay $x={pt_nb_false[0]}; y={pt_nb_false[1]}$ vào bất phương trình ta được ${val} {chosen_sign} {c}$ (không thỏa mãn). Vậy mệnh đề sai.'
                
                if th_da_1 == th_da_1_d:
                    val2 = a*pt_th_true[0] + b*pt_th_true[1]
                    loigiai_th_1 = f'Thay $x={pt_th_true[0]}; y={pt_th_true[1]}$ vào bất phương trình ta được ${val2} {chosen_sign} {c}$ (thỏa mãn). Vậy mệnh đề đúng.'
                else:
                    val3 = a*pt_th_false[0] + b*pt_th_false[1]
                    loigiai_th_1 = f'Thay $x={pt_th_false[0]}; y={pt_th_false[1]}$ vào bất phương trình ta được ${val3} {chosen_sign} {c}$ (không thỏa mãn). Vậy mệnh đề sai.'
                
                if vd_da_1 == vd_da_1_d:
                    loigiai_vd_1 = f'Thay $x=0$ vào bất phương trình ta được ${b}y {chosen_sign} {c} \\Leftrightarrow y {chosen_sign} \\frac{{{c}}}{{{b}}}$. Có vô số giá trị thực của $y$ thỏa mãn. Vậy mệnh đề đúng.'
                else:
                    loigiai_vd_1 = f'Thay $x=0$ vào bất phương trình ta được ${b}y {chosen_sign} {c} \\Leftrightarrow y {chosen_sign} \\frac{{{c}}}{{{b}}}$. Có vô số giá trị thực của $y$ thỏa mãn chứ không phải chỉ có 2. Vậy mệnh đề sai.'
                
                if vdc_da_1 == vdc_da_1_d:
                    loigiai_vdc_1 = f'Bất phương trình có dấu "${chosen_sign}$" nên miền nghiệm {border_status}. Vậy mệnh đề đúng.'
                else:
                    loigiai_vdc_1 = f'Bất phương trình có dấu "${chosen_sign}$" nên miền nghiệm phải {border_status}. Vậy mệnh đề sai.'
                
                # Gán lại vào list và xáo trộn 
                list_nb_1, list_nb_2 = [nb_da_1], [loigiai_nb_1]
                list_th_1, list_th_2 = [th_da_1], [loigiai_th_1]
                list_vd_1, list_vd_2 = [vd_da_1], [loigiai_vd_1]
                list_vdc_1, list_vdc_2 = [vdc_da_1], [loigiai_vdc_1]
                
                combined_nb = list(zip(list_nb_1, list_nb_2))
                combined_th = list(zip(list_th_1, list_th_2))
                combined_vd = list(zip(list_vd_1, list_vd_2))
                combined_vdc = list(zip(list_vdc_1, list_vdc_2))
                
                random.shuffle(combined_nb)
                random.shuffle(combined_th)
                random.shuffle(combined_vd)
                random.shuffle(combined_vdc)
                
                shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
                shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
                shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
                shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
                
                # Xuất câu hỏi: Chữ -> 4 Ý lựa chọn -> Hình vẽ -> Lời giải
                content = ('\\begin{minipage}{\\textwidth} \n'
                    '\\begin{ex}\n'+
                    str(noidungcauhoi)+ '\n'
                    '\\choiceTFn \n'
                    '{'+str(shuffled_answers_nb[0])+'}\n'
                    '{'+str(shuffled_answers_th[0])+'}\n'
                    '{'+str(shuffled_answers_vd[0])+'}\n'
                    '{'+str(shuffled_answers_vdc[0])+'}\n'
                    + str(hinh_ve_tikz) + '\n'
                    '\\loigiai{ \n'
                    '\\begin{enumEX}[a)]{1} \n'
                    '\\item '+str(shuffled_solutions_nb[0])+'\n'
                    '\\item '+str(shuffled_solutions_th[0])+'\n'
                    '\\item '+str(shuffled_solutions_vd[0])+'\n'
                    '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                    '\\end{enumEX}} \n'
                    '\\end{ex}\n'
                    '\\end{minipage}\n\n')
                return content