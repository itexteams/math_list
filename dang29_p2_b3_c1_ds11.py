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


def bt_dang29_p2_b3_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # B3-Suy nghĩ tìm cách random bài toán
            # Để giữ nguyên bản chất lượng giác rút gọn của bài toán: 
            # g(x) = cos(2ax) / (1 - sin(2ax)) = (cos(ax) - sin(ax))(cos(ax) + sin(ax)) / (cos(ax) - sin(ax))^2 
            #      = (cos(ax) + sin(ax)) / (cos(ax) - sin(ax))
            # Ta random hệ số góc a trong khoảng [1, 2] để bài toán đa dạng mà vẫn vừa sức học sinh.
            a_heso = random.choice([1, 2])

            # Thiết lập các chuỗi góc dựa trên hệ số ngẫu nhiên
            if a_heso == 1:
                str_f = "\\cos x + \\sin x"
                str_g = "\\frac{\\cos 2x}{1 - \\sin 2x}"
                str_g_rut_gon_dung = "\\frac{\\sin x + \\cos x}{\\cos x - \\sin x}"
                str_g_rut_gon_sai = "\\frac{\\sin x + \\cos x}{\\sin x - \\cos x}"
                str_chu_ky_dung = "2\\pi"
                str_chu_ky_sai = "\\pi"
                # f(x) = g(x) <=> cos x + sin x = (cos x + sin x)/(cos x - sin x)
                # TH1: cos x + sin x = 0 (loại do đk cos x - sin x != 0)
                # TH2: cos x - sin x = 1 <=> cos(x + pi/4) = sqrt(2)/2 -> 2 họ nghiệm -> 2 điểm biểu diễn
                so_diem_bd_dung = "2 điểm"
                so_diem_bd_sai = "4 điểm"
            else:
                str_f = "\\cos 2x + \\sin 2x"
                str_g = "\\frac{\\cos 4x}{1 - \\sin 4x}"
                str_g_rut_gon_dung = "\\frac{\\sin 2x + \\cos 2x}{\\cos 2x - \\sin 2x}"
                str_g_rut_gon_sai = "\\frac{\\sin 2x + \\cos 2x}{\\sin 2x - \\cos 2x}"
                str_chu_ky_dung = "\\pi"
                str_chu_ky_sai = "2\\pi"
                so_diem_bd_dung = "4 điểm"
                so_diem_bd_sai = "8 điểm"

            # Giá trị lớn nhất luôn là sqrt(2) cho cả 2 trường hợp vì biên độ sin + cos bằng 1
            str_max_dung = "\\sqrt{2}"
            str_max_sai = "2"

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hai hàm số lượng giác $f(x) = %s$ và $g(x) = %s$.\\\\
            Xét tính đúng - sai của các phát biểu sau:''' 
                             % (str_f, str_g))

            ########################################################################
            # Nhận biết ############################################
            nb_da_1_s = '$g(x) = %s$' % (str_g_rut_gon_sai)
            nb_da_1_d = '\\True $g(x) = %s$' % (str_g_rut_gon_dung)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            if a_heso == 1:
                loigiai_nb_1 = ('''Ta có biến đổi cho hàm số $g(x)$:\\\\
            $g(x) = \\frac{\\cos 2x}{1 - \\sin 2x} = \\frac{\\cos^2 x - \\sin^2 x}{(\\cos x - \\sin x)^2} = \\frac{(\\cos x - \\sin x)(\\cos x + \\sin x)}{(\\cos x - \\sin x)^2} = \\frac{\\cos x + \\sin x}{\\cos x - \\sin x}$.''')
            else:
                loigiai_nb_1 = ('''Ta có biến đổi cho hàm số $g(x)$:\\\\
            $g(x) = \\frac{\\cos 4x}{1 - \\sin 4x} = \\frac{\\cos^2 2x - \\sin^2 2x}{(\\cos 2x - \\sin 2x)^2} = \\frac{(\\cos 2x - \\sin 2x)(\\cos 2x + \\sin 2x)}{(\\cos 2x - \\sin 2x)^2} = \\frac{\\cos 2x + \\sin 2x}{\\cos 2x - \\sin 2x}$.''')

            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            th_da_1_d = '\\True Hàm số $f(x)$ có chu kỳ tuần hoàn $T = %s$' % (str_chu_ky_dung)
            th_da_1_s = 'Hàm số $f(x)$ có chu kỳ tuần hoàn $T = %s$' % (str_chu_ky_sai)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            if a_heso == 1:
                loigiai_th_1 = ('''Hàm số $f(x) = \\cos x + \\sin x = \\sqrt{2}\\sin\\left(x + \\frac{\\pi}{4}\\right)$.\\\\
            Hàm số lượng giác $y = \\sin x$ có chu kỳ tuần hoàn là $T = 2\\pi$. Do đó hàm số $f(x)$ cũng có chu kỳ tuần hoàn là $T = 2\\pi$.''')
            else:
                loigiai_th_1 = ('''Hàm số $f(x) = \\cos 2x + \\sin 2x = \\sqrt{2}\\sin\\left(2x + \\frac{\\pi}{4}\\right)$.\\\\
            Hàm số lượng giác dạng $y = \\sin(kx)$ có chu kỳ tuần hoàn là $T = \\frac{2\\pi}{|k|}$.\\\\
            Với $k = 2$, chu kỳ tuần hoàn của hàm số $f(x)$ là $T = \\frac{2\\pi}{2} = \\pi$.''')

            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng ############################################
            vd_da_1_d = '\\True Hàm số $f(x)$ có giá trị lớn nhất bằng $%s$' % (str_max_dung)
            vd_da_1_s = 'Hàm số $f(x)$ có giá trị lớn nhất bằng $%s$' % (str_max_sai)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            if a_heso == 1:
                loigiai_vd_1 = ('''Sử dụng công thức biến đổi tổng thành tích:\\\\
            $f(x) = \\sin x + \\cos x = \\sqrt{2}\\sin\\left(x + \\frac{\\pi}{4}\\right)$.\\\\
            Vì $-1 \\le \\sin\\left(x + \\frac{\\pi}{4}\\right) \\le 1$ nên $-\\sqrt{2} \\le f(x) \\le \\sqrt{2}$.\\\\
            Vậy giá trị lớn nhất của hàm số $f(x)$ bằng $\\sqrt{2}$.''')
            else:
                loigiai_vd_1 = ('''Sử dụng công thức biến đổi tổng thành tích:\\\\
            $f(x) = \\sin 2x + \\cos 2x = \\sqrt{2}\\sin\\left(2x + \\frac{\\pi}{4}\\right)$.\\\\
            Vì $-1 \\le \\sin\\left(2x + \\frac{\\pi}{4}\\right) \\le 1$ nên $-\\sqrt{2} \\le f(x) \\le \\sqrt{2}$.\\\\
            Vậy giá trị lớn nhất của hàm số $f(x)$ bằng $\\sqrt{2}$.''')

            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao ############################################
            vdc_da_1_d = '\\True Phương trình $f(x) = g(x)$ có %s biểu diễn nghiệm trên vòng tròn lượng giác' % (so_diem_bd_dung)
            vdc_da_1_s = 'Phương trình $f(x) = g(x)$ có %s biểu diễn nghiệm trên vòng tròn lượng giác' % (so_diem_bd_sai)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            if a_heso == 1:
                loigiai_vdc_1 = ('''Điều kiện xác định của phương trình: $1 - \\sin 2x \\neq 0 \\Leftrightarrow \\sin 2x \\neq 1 \\Leftrightarrow x \\neq \\frac{\\pi}{4} + k\\pi$.\\\\
            Khi đó phương trình hoành độ giao điểm trở thành:\\\\
            $\\sin x + \\cos x = \\frac{\\sin x + \\cos x}{\\cos x - \\sin x} \\Leftrightarrow (\\sin x + \\cos x)\\left(1 - \\frac{1}{\\cos x - \\sin x}\\right) = 0$\\\\
            - Trường hợp 1: $\\sin x + \\cos x = 0 \\Leftrightarrow \\tan x = -1 \\Leftrightarrow x = -\\frac{\\pi}{4} + k\\pi$. Nghiệm này thỏa mãn điều kiện xác định và cho chúng ta $2$ điểm biểu diễn.\\\\
            - Trường hợp 2: $\\cos x - \\sin x = 1 \\Leftrightarrow \\sqrt{2}\\cos\\left(x + \\frac{\\pi}{4}\\right) = 1 \\Leftrightarrow \\cos\\left(x + \\frac{\\pi}{4}\\right) = \\frac{\\sqrt{2}}{2}$.\\\\
            Suy ra $x + \\frac{\\pi}{4} = \\pm\\frac{\\pi}{4} + k2\\pi \\Leftrightarrow x = k2\\pi$ (thỏa mãn) hoặc $x = -\\frac{\\pi}{2} + k2\\pi$ (thỏa mãn). Hai họ nghiệm này cho thêm $2$ điểm biểu diễn khác.\\\\
            Kết hợp điều kiện và loại bỏ các nghiệm trùng, phương trình có tổng cộng %s biểu diễn nghiệm trên đường tròn lượng giác.''' % (so_diem_bd_dung))
            else:
                loigiai_vdc_1 = ('''Điều kiện xác định của phương trình: $1 - \\sin 4x \\neq 0 \\Leftrightarrow \\sin 4x \\neq 1 \\Leftrightarrow x \\neq \\frac{\\pi}{8} + k\\frac{\\pi}{2}$.\\\\
            Khi đó phương trình hoành độ giao điểm trở thành:\\\\
            $\\sin 2x + \\cos 2x = \\frac{\\sin 2x + \\cos 2x}{\\cos 2x - \\sin 2x} \\Leftrightarrow (\\sin 2x + \\cos 2x)\\left(1 - \\frac{1}{\\cos 2x - \\sin 2x}\\right) = 0$\\\\
            - Trường hợp 1: $\\sin 2x + \\cos 2x = 0 \\Leftrightarrow \\tan 2x = -1 \\Leftrightarrow 2x = -\\frac{\\pi}{4} + k\\pi \\Leftrightarrow x = -\\frac{\\pi}{8} + k\\frac{\\pi}{2}$. Nghiệm này thỏa mãn điều kiện xác định và cho chúng ta $4$ điểm biểu diễn.\\\\
            - Trường hợp 2: $\\cos 2x - \\sin 2x = 1 \\Leftrightarrow \\sqrt{2}\\cos\\left(2x + \\frac{\\pi}{4}\\right) = 1 \\Leftrightarrow \\cos\\left(2x + \\frac{\\pi}{4}\\right) = \\frac{\\sqrt{2}}{2}$.\\\\
            Suy ra $2x + \\frac{\\pi}{4} = \\pm\\frac{\\pi}{4} + k2\\pi \\Leftrightarrow x = k\\pi$ (thỏa mãn) hoặc $x = -\\frac{\\pi}{4} + k\\pi$ (thỏa mãn). Các họ nghiệm này cho thêm $4$ điểm biểu diễn.\\\\
            Kết hợp tất cả điều kiện, phương trình có tổng cộng %s biểu diễn nghiệm trên đường tròn lượng giác.''' % (so_diem_bd_dung))

            list_vdc_2 = [loigiai_vdc_1]

            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
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
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

