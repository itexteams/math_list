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


def bt_dang41_p2_b3_c3_ds12(self):
            # --- BƯỚC 1: CHỌN THÔNG SỐ NGẪU NHIÊN ---
            # Khai báo biến
            t = symbols('t')
            R_mm = random.choice([100, 150, 200, 250])
            h_cone_mm = random.choice([200, 300, 400])
            t_end = random.choice([2, 4, 6])
            a_val = -Rational(random.choice([1, 3, 5]), 2) # -0.5, -1.5, -2.5
            b_val = -2 * a_val * t_end / 2 # To make max at t_end/2

            vt_expr = a_val * t**2 + b_val * t
            D_mm = 2 * R_mm

            def fmt_dec(val, places=2):
                f = float(val)
                s = f"{f:.{places}f}".rstrip('0').rstrip('.')
                if s == '': s = '0'
                return s.replace('.', ',')

            vt_latex = latex(vt_expr).replace('.', ',')
            t_max = -b_val / (2 * a_val)
            v_max = vt_expr.subs(t, t_max)

            h_rain = sp.integrate(vt_expr, (t, 0, t_end))
            R_cm = R_mm / 10
            h_rain_cm = float(h_rain) / 10
            V_water_cm3 = sp.pi * (R_cm**2) * h_rain_cm

            hx_expr = sp.cbrt(3 * V_water_cm3 / sp.pi * (h_cone_mm / R_mm)**2) * 10
            hx_mm = float(hx_expr)

            str_vmax = fmt_dec(v_max)
            str_h_rain = fmt_dec(h_rain)
            str_V_water = fmt_dec(float(V_water_cm3 / sp.pi))
            str_hx = fmt_dec(round(hx_mm))

            # Nội dung câu hỏi
            noidungcauhoi = ('''\\immini{Tại một trạm quan trắc khí tượng, các kỹ sư sử dụng một dụng cụ đo mưa chuyên dụng có dạng hình nón ngược với đường kính miệng nón bằng $%s$ mm và chiều cao khối nón bằng $%s$ mm. Vào một buổi chiều mùa hạ, có một cơn mưa rào kéo dài trong đúng $%s$ giờ. Các thiết bị cảm biến đo được cường độ mưa biến thiên theo thời gian được mô tả bởi công thức $v(t) = %s$ (đơn vị: mm/giờ), trong đó $t$ là thời gian tính từ lúc bắt đầu mưa. Giả sử ban đầu dụng cụ đo khô ráo, không có nước.}
            {\\begin{tikzpicture}[scale=0.6, thick]
                \\def\\R{2.5}
                \\def\\h{6}
                \\def\\r{1.5}
                \\def\\hw{3.6}
                \\draw (-\\R, \\h) arc (180:360:\\R cm and 0.6cm);
                \\draw[dashed] (\\R, \\h) arc (0:180:\\R cm and 0.6cm);
                \\draw (-\\R, \\h) -- (0,0) -- (\\R, \\h);
                \\fill[cyan!50, opacity=0.7] (-\\r, \\hw) arc (180:360:\\r cm and 0.4cm) -- (0,0) -- cycle;
                \\draw[cyan!80!blue] (-\\r, \\hw) arc (180:360:\\r cm and 0.4cm);
                \\draw[cyan!80!blue, dashed] (\\r, \\hw) arc (0:180:\\r cm and 0.4cm);
                \\fill[cyan!30, opacity=0.7] (0,\\hw) ellipse (\\r cm and 0.4cm);
                \\draw[|-|] (-\\R, \\h+1.5) -- (\\R, \\h+1.5) node[midway, fill=white] {$%s$ mm};
                \\draw[|-|] (-\\R-1.5, 0) -- (-\\R-1.5, \\h) node[midway, fill=white] {$%s$ mm};
                \\draw[dashed] (-\\R, \\h) -- (-\\R-1.5, \\h);
                \\draw[dashed] (0, 0) -- (-\\R-1.5, 0);
                \\draw[dashed] (-\\R, \\h+1.5) -- (-\\R, \\h);
                \\draw[dashed] (\\R, \\h+1.5) -- (\\R, \\h);
            \\end{tikzpicture} }''' % (D_mm, h_cone_mm, t_end, vt_latex, D_mm, h_cone_mm))


            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Cường độ mưa lớn nhất trong suốt trận mưa này đạt $%s$ mm/giờ' % str_vmax
            nb_da_1_s = 'Cường độ mưa lớn nhất trong suốt trận mưa này đạt $%s$ mm/giờ' % fmt_dec(v_max + random.choice([1, 2]))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Xét hàm số $v(t) = %s$ có đồ thị là parabol bề lõm quay xuống, đạt cực đại tại $t = %s$.\\\\
            Suy ra $v_{\\max}(%s) = %s$ (mm/giờ) nên \\textbf{mệnh đề a) đúng}.''' % (vt_latex, fmt_dec(t_max), fmt_dec(t_max), str_vmax))

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Tổng lượng mưa của cả trận mưa là $%s$ mm' % str_h_rain
            th_da_1_s = 'Tổng lượng mưa của cả trận mưa là $%s$ mm' % fmt_dec(h_rain + random.choice([-2, 2.5, 3]))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Gọi $h$ (mm) là tổng lượng mưa của cả trận: $h = \\int\\limits_0^{%s} \\left(%s\\right) \\mathrm{d}t = %s$ (mm) nên \\textbf{mệnh đề b) %s}.''' % (t_end, vt_latex, str_h_rain, 'đúng' if '\\True' in th_da_1 else 'sai'))

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Thể tích nước mưa thực tế thu được trong dụng cụ đo sau $%s$ giờ là $%s\\pi$ (cm$^3$)' % (t_end, str_V_water)
            vd_da_1_s = 'Thể tích nước mưa thực tế thu được trong dụng cụ đo sau $%s$ giờ là $%s\\pi$ (cm$^3$)' % (t_end, fmt_dec(float(V_water_cm3/sp.pi) + random.choice([10, 20])))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Dụng cụ đo có miệng hình tròn bán kính $R = %s$ mm $= %s$ (cm).\\\\
            Lượng mưa $h = %s$ mm $= %s$ cm là độ cao nước rơi xuống trên một đơn vị diện tích bề mặt ngang.\\\\
            Thể tích nước thu được trong phễu chính bằng diện tích miệng phễu nhân với chiều cao lượng mưa: $V = \\pi . %s^2 . %s = %s\\pi$ (cm$^3$) nên \\textbf{mệnh đề c) %s}.''' % (R_mm, fmt_dec(R_cm), str_h_rain, fmt_dec(h_rain_cm), fmt_dec(R_cm), fmt_dec(h_rain_cm), str_V_water, 'đúng' if '\\True' in vd_da_1 else 'sai'))

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Kết thúc trận mưa, mực nước trong dụng cụ đo dâng lên đến chiều cao $%s$ mm (Kết quả làm tròn đến hàng đơn vị)' % str_hx
            vdc_da_1_s = 'Kết thúc trận mưa, mực nước trong dụng cụ đo dâng lên đến chiều cao $%s$ mm (Kết quả làm tròn đến hàng đơn vị)' % fmt_dec(round(hx_mm) + random.choice([-5, 5]))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Gọi $h_x$ là chiều cao, $r$ là bán kính tương ứng thì theo định lý Talet: $\\frac{r}{R} = \\frac{h_x}{h} \\Rightarrow r = \\frac{R h_x}{h}$.\\\\
            Thể tích nước trong phễu theo $h_x$: $V = \\frac{1}{3} \\pi r^2 h_x = \\frac{1}{3} \\pi \\left( \\frac{%s h_x}{%s} \\right)^2 h_x = %s\\pi \\Rightarrow h_x \\approx %s$ (mm)\\\\
            nên \\textbf{mệnh đề d) %s}.''' % (R_mm, h_cone_mm, str_V_water, str_hx, 'đúng' if '\\True' in vdc_da_1 else 'sai'))

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
                str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
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

