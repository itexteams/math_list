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


def bt_dang17_p2_b4_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến toán học
            x = symbols('x')

            # B3-Suy nghĩ tìm cách random bài toán:
            # Hàm số gốc có dạng f(x) = sin^4(x/2) + cos^4(x/2)
            # Biến đổi tổng quát: sin^4(u) + cos^4(u) = 1 - 1/2*sin^2(2u) = 1 - 1/4*(1 - \cos(4u)) = 3/4 + 1/4*\cos(4u)
            # Ta random mẫu số k trong góc (x/k). Trong ảnh mẫu là k = 2.
            # Ta có thể chọn ngẫu nhiên k trong các số [1, 2, 4] để bài toán đẹp và vừa sức.

            k = random.choice([1, 2, 4])

            # Biến biểu thức góc trong sin, cos
            if k == 1:
                goc_str = 'x'
                chu_ky = '\\pi'          # T = 2pi / 2 = pi
                goc_cos = '4x'
            else:
                goc_str = '\\frac{x}{%s}' % (latex(k))
                if k == 2:
                    chu_ky = '\\pi'      # T = 2pi / 2 = pi
                    goc_cos = '2x'
                elif k == 4:
                    chu_ky = '2\\pi'     # T = 2pi / 1 = 2pi
                    goc_cos = 'x'

            # Các thông số cố định cho dạng sin^4 + cos^4
            gtln = '1'
            gtnn = '\\frac{1}{2}'
            f_0 = '1'

            # Tính toán cho câu d: f(x) = 5/8 
            # 3/4 + 1/4*cos(2u) = 5/8 => 1/4*cos(2u) = -1/8 => cos(2u) = -1/2
            # Với u = x/k => 4u = (4/k)*x
            # Nếu k=2 => cos(2x) = -1/2. Nghiệm trên (0, 2pi) là 2x = 2pi/3, 4pi/3, 8pi/3, 10pi/3 => x = pi/3, 2pi/3, 4pi/3, 5pi/3. Tổng nghiệm = 4pi.
            # Để giữ tính đa dạng và chuẩn xác cho từng trường hợp random, ta tính tổng nghiệm trên khoảng (0, 2pi):
            if k == 1:
                # cos(4x) = -1/2 => 4x thuộc (0, 8pi) -> có 8 nghiệm. Tổng nghiệm là 8pi.
                tong_nghiem = '8\\pi'
                tong_nghiem_sai = '4\\pi'
            elif k == 2:
                # cos(2x) = -1/2 => 2x thuộc (0, 4pi) -> có 4 nghiệm: pi/3, 2pi/3, 4pi/3, 5pi/3. Tổng bằng 4pi.
                tong_nghiem = '4\\pi'
                tong_nghiem_sai = '6\\pi'
            elif k == 4:
                # cos(x) = -1/2 => x thuộc (0, 2pi) -> có 2 nghiệm: 2pi/3, 4pi/3. Tổng bằng 2pi.
                tong_nghiem = '2\\pi'
                tong_nghiem_sai = '3\\pi'

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $f(x)=\\sin^4 %s + \\cos^4 %s$. Xét tính đúng, sai của các mệnh đề sau:'''
                             % (goc_str, goc_str))

            ########################################################################
            # Nhận biết ############################################
            nb_da_1_d = '\\True Đồ thị hàm số đi qua điểm $A(0;1)$'
            nb_da_1_s = 'Đồ thị hàm số đi qua điểm $A(0;0)$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Thay $x = 0$ vào hàm số ta được $f(0) = \\sin^4 0 + \\cos^4 0 = 0 + 1 = 1$.\\\\
            Do đó đồ thị hàm số đi qua điểm $A(0;1)$.''')

            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            th_da_1_d = '\\True Hàm số có chu kỳ bằng $T = %s$' % (chu_ky)
            th_da_1_s = 'Hàm số có chu kỳ bằng $T = 2\\pi$' if chu_ky != '2\\pi' else 'Hàm số có chu kỳ bằng $T = \\pi$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            loigiai_th_1 = ('''Ta biến đổi hàm số:\\\\
            $f(x) = \\left(\\sin^2 %s + \\cos^2 %s\\right)^2 - 2\\sin^2 %s \\cdot \\cos^2 %s$\\\\
            $= 1 - \\frac{1}{2}\\sin^2 \\left(2 \\cdot %s\\right) = 1 - \\frac{1}{2} \\cdot \\frac{1-\\cos %s}{2} = \\frac{3}{4} + \\frac{1}{4}\\cos %s$.\\\\
            Hàm số $y = \\cos %s$ tuần hoàn với chu kỳ $T = %s$.'''
                            % (goc_str, goc_str, goc_str, goc_str, goc_str, goc_cos, goc_cos, goc_cos, chu_ky))

            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng ############################################
            vd_da_1_d = '\\True Hàm số có giá trị lớn nhất bằng $%s$' % (gtln)
            vd_da_1_s = 'Hàm số có giá trị lớn nhất bằng $%s$' % (gtnn)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Từ biểu thức rút gọn $f(x) = \\frac{3}{4} + \\frac{1}{4}\\cos %s$, do $-1 \\le \\cos %s \\le 1$ nên:\\\\
            $\\frac{3}{4} + \\frac{1}{4} \\cdot (-1) \\le f(x) \\le \\frac{3}{4} + \\frac{1}{4} \\cdot 1 \\Leftrightarrow \\frac{1}{2} \\le f(x) \\le 1$.\\\\
            Vậy giá trị lớn nhất của hàm số bằng $1$.'''
                            % (goc_cos, goc_cos))

            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao ############################################
            vdc_da_1_d = '\\True Tổng tất cả các nghiệm thuộc khoảng $(0;2\\pi)$ của phương trình $f(x)=\\frac{5}{8}$ là $%s$' % (tong_nghiem)
            vdc_da_1_s = 'Tổng tất cả các nghiệm thuộc khoảng $(0;2\\pi)$ của phương trình $f(x)=\\frac{5}{8}$ là $%s$' % (tong_nghiem_sai)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            # Lời giải chi tiết động theo cấu trúc k random
            if k == 1:
                loigiai_vdc_1 = ('''Phương trình $f(x) = \\frac{5}{8} \\Leftrightarrow \\frac{3}{4} + \\frac{1}{4}\\cos 4x = \\frac{5}{8} \\Leftrightarrow \\cos 4x = -\\frac{1}{2}$.\\\\
            Vì $x \\in (0;2\\pi) \\Rightarrow 4x \\in (0;8\\pi)$.\\\\
            Các nghiệm của phương trình là $4x \\in \\left\\{ \\frac{2\\pi}{3}; \\frac{4\\pi}{3}; \\frac{8\\pi}{3}; \\frac{10\\pi}{3}; \\frac{14\\pi}{3}; \\frac{16\\pi}{3}; \\frac{20\\pi}{3}; \\frac{22\\pi}{3} \\right\\}$.\\\\
            Chia cho $4$ để tìm các nghiệm $x$, sau đó cộng lại ta được tổng các nghiệm bằng $8\\pi$.''')
            elif k == 2:
                loigiai_vdc_1 = ('''Phương trình $f(x) = \\frac{5}{8} \\Leftrightarrow \\frac{3}{4} + \\frac{1}{4}\\cos 2x = \\frac{5}{8} \\Leftrightarrow \\cos 2x = -\\frac{1}{2}$.\\\\
            Vì $x \\in (0;2\\pi) \\Rightarrow 2x \\in (0;4\\pi)$.\\\\
            Các giá trị của $2x$ thỏa mãn là: $2x \\in \\left\\{ \\frac{2\\pi}{3}; \\frac{4\\pi}{3}; \\frac{8\\pi}{3}; \\frac{10\\pi}{3} \\right\\}$.\\\\
            Suy ra $x \\in \\left\\{ \\frac{\\pi}{3}; \\frac{2\\pi}{3}; \\frac{4\\pi}{3}; \\frac{5\\pi}{3} \\right\\}$.\\\\
            Tổng tất cả các nghiệm này bằng $\\frac{\\pi}{3} + \\frac{2\\pi}{3} + \\frac{4\\pi}{3} + \\frac{5\\pi}{3} = 4\\pi$.''')
            elif k == 4:
                loigiai_vdc_1 = ('''Phương trình $f(x) = \\frac{5}{8} \\Leftrightarrow \\frac{3}{4} + \\frac{1}{4}\\cos x = \\frac{5}{8} \\Leftrightarrow \\cos x = -\\frac{1}{2}$.\\\\
            Vì $x \\in (0;2\\pi)$, các nghiệm thỏa mãn phương trình là $x = \\frac{2\\pi}{3}$ hoặc $x = \\frac{4\\pi}{3}$.\\\\
            Tổng tất cả các nghiệm này bằng $\\frac{2\\pi}{3} + \\frac{4\\pi}{3} = 2\\pi$.''')

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

