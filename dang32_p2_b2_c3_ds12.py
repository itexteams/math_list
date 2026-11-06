import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

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


def bt_dang32_p2_b2_c3_ds12(self):
            # Khai báo biến
            # Hàm hỗ trợ định dạng số thập phân có dấu phẩy cho hệ thống VN
            def to_vn_num(num):
                if isinstance(num, float):
                    if num.is_integer():
                        return str(int(num))
                    return str(num).replace('.', ',')
                return str(num)

            # Khai báo biến và Random dữ liệu
            v_1 = random.choice([120, 150, 180, 200]) # Vận tốc sau khi tăng tốc
            v_3 = random.choice([20, 30, 40]) # Vận tốc sau khi hãm phanh
            s_1_km = random.choice([1.0, 1.2, 1.5, 2.0]) # km
            s_1_m = int(s_1_km * 1000)
            s_2_km = random.choice([80, 100, 120]) # km
            s_2_m = s_2_km * 1000
            s_3_km = random.choice([3, 4, 5, 6]) # km
            s_3_m = s_3_km * 1000
            s_4_m = random.choice([300, 480, 500, 600]) # m

            # Tính toán các giá trị thời gian và gia tốc chính xác
            t_1_val = Rational(2 * s_1_m, v_1)
            t_2_val = Rational(s_2_m, v_1)
            t_3_val = Rational(3 * s_3_m, v_3 + 2 * v_1)
            t_4_val = Rational(s_4_m, v_3)

            at32 = v_3 - v_1 # Giá trị at_3^2 (âm)
            at32_pos = abs(at32) # Trị tuyệt đối

            # Tính a làm tròn
            a_val = Rational(at32, 1) / (t_3_val**2)
            a_round = round(float(a_val), 2)
            a_round_str = f"{a_round:.2f}".replace('.', ',')
            a_round_false = a_round + random.choice([0.05, -0.05, 0.1, -0.1])
            a_round_false_str = f"{a_round_false:.2f}".replace('.', ',')

            # Tổng thời gian
            total_time_val = t_1_val + t_2_val + t_3_val + t_4_val
            total_time_round = round(float(total_time_val))
            total_time_false = total_time_round + random.choice([25, 30, -20, 50])

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một khoang tàu Hyperloop thế hệ mới dài $20$ m thực hiện một hành trình trong đường ống chân không. Khoang tàu được gia tốc đều từ trạng thái đứng yên bằng hệ thống phóng điện từ trên quãng đường dài $%s$ km và đạt vận tốc $%s$ m/s. Tàu tiếp tục di chuyển với vận tốc không đổi $%s$ m/s trên quãng đường $%s$ km tiếp theo. Sau đó, tàu bắt đầu kích hoạt hệ thống hãm phanh từ trường làm nó giảm tốc đều từ $%s$ m/s xuống còn $%s$ m/s trên một quãng đường dài $%s$ km. Vận tốc chuyển động của tàu trong giai đoạn này được cho bởi công thức $v(t) = at^2 + %s$ (m/s) với $t$ là thời gian tính từ lúc bắt đầu hãm phanh. Trước khi vào khu vực nhà ga, tàu phải đi qua một đường hầm an toàn dài $%s$ m với vận tốc không đổi là $%s$ m/s.'''               
                             %(to_vn_num(s_1_km), v_1, v_1, to_vn_num(s_2_km), v_1, v_3, to_vn_num(s_3_km), v_1, s_4_m, v_3))

            ########################################################################
            # Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Thời gian để tàu hoàn thành giai đoạn tăng tốc đầu tiên là $%s$ giây' % latex(t_1_val)
            nb_da_1_s = 'Thời gian để tàu hoàn thành giai đoạn tăng tốc đầu tiên là $%s$ giây' % latex(t_1_val + random.choice([5, 10, 15]))
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Vận tốc ban đầu: $v(0)=0$ và quãng đường ban đầu $s(0)=0$ với gia tốc $a_1$ không đổi.\\\\
            Khi đó $v(t) = \\int a_1 \\text{d}t = a_1 t$ với $v(0)=0$ nên $s(t) = \\int v(t) \\text{d}t = \\int a_1 t \\text{d}t = \\frac{1}{2}a_1 t^2 \\ (s(0)=0)$\\\\
            Tại thời điểm kết thúc $t=t_1$ thì $v(t_1)=a_1 t_1=%s \\ (1)$ và $s(t_1)=\\frac{1}{2}a_1 t_1^2=%s \\ (2)$\\\\
            Thay (1) vào (2) $\\Rightarrow \\frac{1}{2} \\cdot %s \\cdot t_1 = %s \\Rightarrow t_1 = %s$ giây.'''
                       %(v_1, s_1_m, v_1, s_1_m, latex(t_1_val)))

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Gia tốc của tàu trong giai đoạn giảm tốc là $%s \\ (\\text{m/s}^2)$ (Kết quả làm tròn đến hàng phần trăm)' % a_round_str
            th_da_1_s = 'Gia tốc của tàu trong giai đoạn giảm tốc là $%s \\ (\\text{m/s}^2)$ (Kết quả làm tròn đến hàng phần trăm)' % a_round_false_str
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Trong giai đoạn này: $v(t) = at^2 + %s$\\\\
            Tại thời điểm $t = t_3$ có vận tốc là $v(t_3) = %s \\Rightarrow at_3^2 + %s = %s \\Leftrightarrow at_3^2 = %s \\ (*)$\\\\
            Quãng đường giảm tốc : $s(t_3) = \\int\\limits_0^{t_3} (at^2 + %s) \\text{d}t = \\frac{1}{3} at_3^3 + %s t_3 = %s \\ (**)$\\\\
            Thay $(*)$ vào $(**) \\Leftrightarrow \\frac{1}{3}(%s)t_3 + %s t_3 = %s \\Rightarrow t_3 = %s$\\\\
            Từ $(*)\\Rightarrow a = \\frac{%s}{t_3^2} = \\frac{%s}{\\left(%s\\right)^2} \\approx %s$.'''       
                       %(v_1, v_3, v_1, v_3, at32, v_1, v_1, s_3_m, at32, v_1, s_3_m, latex(t_3_val), at32, at32, latex(t_3_val), a_round_str))

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## 
            # Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Tổng thời gian thực hiện cả hành trình của tàu là $%s$ giây (Kết quả làm tròn đến hàng đơn vị)' % total_time_round
            vd_da_1_s = 'Tổng thời gian thực hiện cả hành trình của tàu là $%s$ giây (Kết quả làm tròn đến hàng đơn vị)' % total_time_false
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Giai đoạn 1 (tăng tốc): $t_1 = %s$ (giây); giai đoạn 2 (vận tốc không đổi): $t_2 = \\frac{%s}{%s} = %s$ (giây)\\\\
            Giai đoạn 3 (giảm tốc): $t_3 = %s$ (giây); giai đoạn 4 (vận tốc không đổi cuối): $t_4 = \\frac{%s}{%s} = %s$ (giây)\\\\
            Tổng thời gian thực hiện hành trình là: $T = t_1 + t_2 + t_3 + t_4 = %s + %s + %s + %s \\approx %s$ (giây).''' 
                       %(latex(t_1_val), s_2_m, v_1, latex(t_2_val), latex(t_3_val), s_4_m, v_3, latex(t_4_val), latex(t_1_val), latex(t_2_val), latex(t_3_val), latex(t_4_val), total_time_round))

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## 
            # Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Trong giai đoạn giảm tốc, độ lớn gia tốc tức thời lớn nhất của tàu gấp đôi độ lớn gia tốc trung bình của cả giai đoạn đó' 
            vdc_da_1_s = 'Trong giai đoạn giảm tốc, độ lớn gia tốc tức thời lớn nhất của tàu bằng độ lớn gia tốc trung bình của cả giai đoạn đó' 
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Gia tốc tức thời: $a(t) = v'(t) = 2at$ nên độ lớn cực đại tại $t = t_3 \\Rightarrow |a_{\\max}| = |2at_3| = 2|a|t_3 \\ (1)$.\\\\
            Gia tốc trung bình trong giai đoạn này: $a_{tb} = \\frac{v(t_3) - v(0)}{t_3 - 0} = \\frac{%s - %s}{t_3} = \\frac{%s}{t_3}$.\\\\
            Độ lớn: $|a_{tb}| = \\left| \\frac{%s}{t_3} \\right| = \\frac{%s}{t_3}$.\\\\
            Từ dữ kiện đề bài: $v(t_3) = %s \\Rightarrow at_3^2 + %s = %s \\Leftrightarrow at_3^2 = %s \\Leftrightarrow |a|t_3 = \\frac{%s}{t_3}$.\\\\
            Thay $|a|t_3 = \\frac{%s}{t_3}$ vào $(1) \\Rightarrow |a_{\\max}| = 2|a_{tb}|$.'''
                       %(v_3, v_1, at32, at32, at32_pos, v_3, v_1, v_3, at32, at32_pos, at32_pos))

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vdc)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

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

            # Gán lại vào list
            list_nb_1 = [nb_da_1]
            list_th_1 = [th_da_1]
            list_vd_1 = [vd_da_1]
            list_vdc_1 = [vdc_da_1]

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

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ '\n'
                '\\choiceTFn \n'
                '{'+str(shuffled_answers_nb[0])+'}\n'
                '{'+str(shuffled_answers_th[0])+'}\n'
                '{'+str(shuffled_answers_vd[0])+'}\n'
                '{'+str(shuffled_answers_vdc[0])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n\\end{minipage}\n\n')
            return content

