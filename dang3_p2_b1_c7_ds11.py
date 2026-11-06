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


def bt_dang3_p2_b1_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến
            t = symbols('t')

            # --- BƯỚC 1: TẠO DỮ LIỆU NGẪU NHIÊN ---
            # Chọn nghiệm của v(t) để số liệu đẹp: v(t) = (t - t2)(t - t1) = t^2 - (t1+t2)t + t1*t2
            # Để giống mẫu: s'(t) = t^2 - 2At - B. Vậy 2A = t1+t2, B = -t1*t2
            t2 = random.randint(5, 9) # Nghiệm dương (thời điểm vận tốc triệt tiêu)
            t1 = -random.randint(1, 3) # Nghiệm âm

            A_val = Rational(t1 + t2, 2)
            B_val = -t1 * t2
            C_val = random.randint(2, 10)

            # Hàm số quãng đường S(t) = t^3/3 - A*t^2 - B*t - C
            s_func = Rational(1, 3)*t**3 - A_val*t**2 - B_val*t - C_val
            v_func = diff(s_func, t)
            a_func = diff(v_func, t)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một vật chuyển động thẳng xác định bởi phương trình $S = s\\left( t \\right) = %s$ trong đó $t$ được tính bằng giây và $S$ được tính bằng mét.''' 
                             % (latex(s_func)))

            ########################################################################
            # Nhận biết: Tính vận tốc tại thời điểm t0
            t_nb = t2 + 2
            v_nb_dung = v_func.subs(t, t_nb)
            v_nb_sai = v_nb_dung + random.choice([-5, 5, 10])

            nb_da_1_d = '\\True Vận tốc tại thời điểm $t = %s$s là $%s$m/s' % (latex(t_nb), latex(v_nb_dung))
            nb_da_1_s = 'Vận tốc tại thời điểm $t = %s$s là $%s$m/s' % (latex(t_nb), latex(v_nb_sai))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Vận tốc của vật là $v\\left( t \\right) = s'\\left( t \\right) = %s$.\\\\
            Tại thời điểm $t = %s$s, vận tốc là $v\\left( %s \\right) = %s$ m/s.'''
                            % (latex(v_func), latex(t_nb), latex(t_nb), latex(v_nb_dung)))

            ########################################################################
            # Thông hiểu: Tính gia tốc tại thời điểm t1
            t_th = t2 + 1
            a_th_dung = a_func.subs(t, t_th)
            a_th_sai = a_th_dung + random.choice([-2, 2, 4])

            th_da_1_d = '\\True Gia tốc tại thời điểm $t = %s$s là $%s$m/s$^{2}$' % (latex(t_th), latex(a_th_dung))
            th_da_1_s = 'Gia tốc tại thời điểm $t = %s$s là $%s$m/s$^{2}$' % (latex(t_th), latex(a_th_sai))
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Gia tốc của vật là $a\\left( t \\right) = v'\\left( t \\right) = %s$.\\\\
            Tại thời điểm $t = %s$s, gia tốc là $a\\left( %s \\right) = %s$ m/s$^{2}$.'''
                            % (latex(a_func), latex(t_th), latex(t_th), latex(a_th_dung)))

            ########################################################################
            # Vận dụng: Gia tốc khi vận tốc triệt tiêu (v=0)
            # Vận tốc triệt tiêu tại t = t2
            a_vd_dung = a_func.subs(t, t2)
            a_vd_sai = a_vd_dung + random.choice([-1, 1, 3])

            vd_da_1_d = '\\True Gia tốc tại thời điểm vận tốc triệt tiêu là $%s$m/s$^{2}$' % (latex(a_vd_dung))
            vd_da_1_s = 'Gia tốc tại thời điểm vận tốc triệt tiêu là $%s$m/s$^{2}$' % (latex(a_vd_sai))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Vận tốc triệt tiêu khi $v\\left( t \\right) = 0 \\Leftrightarrow %s = 0 \\Leftrightarrow t = %s$ (giây) vì $t > 0$.\\\\
            Gia tốc tại thời điểm đó là $a\\left( %s \\right) = %s$ m/s$^{2}$.'''
                            % (latex(v_func), latex(t2), latex(t2), latex(a_vd_dung)))

            ########################################################################
            # Vận dụng cao: Thời điểm vận tốc cực tiểu
            t_min_v = A_val
            t_sai_v = t_min_v + 1

            vdc_da_1_d = '\\True Tại thời điểm $t = %s$s thì vận tốc của vật là nhỏ nhất' % (latex(t_min_v))
            vdc_da_1_s = 'Tại thời điểm $t = %s$s thì vận tốc của vật là nhỏ nhất' % (latex(t_sai_v))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Xét hàm vận tốc $v\\left( t \\right) = %s$. Đây là một hàm số bậc hai có đồ thị là parabol với bề lõm hướng lên trên.\\\\
            Vận tốc đạt giá trị nhỏ nhất tại đỉnh của parabol: $t = -\\frac{b}{2a} = %s$s.\\\\
            Bảng biến thiên của vận tốc:\\\\
            \\begin{tikzpicture}[line width=1pt]
            \\tkzTabInit[espcl=2.5,lgt=1.5]
            {$t$/1,$v'\\left( t \\right)$/0.7,$v\\left( t \\right)$/2}
            {$0$,$%s$,$+\\infty$}
            \\tkzTabLine{,-,0,+}
            \\tkzTabVar{+/$v\\left( 0 \\right)$,-/$v\\left( %s \\right)$,+/$+\\infty$}
            \\end{tikzpicture}'''
                             % (latex(v_func), latex(t_min_v), latex(t_min_v), latex(t_min_v)))

            # --- BƯỚC 2: LOGIC XÁO TRỘN VÀ KIỂM TRA ĐIỀU KIỆN ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)

                if 1 <= count_true_answers([nb_sel, th_sel, vd_sel, vdc_sel]) <= 3:
                    break

            # Gán lời giải tương ứng
            sol_nb = loigiai_nb_1
            sol_th = loigiai_th_1
            sol_vd = loigiai_vd_1
            sol_vdc = loigiai_vdc_1

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(nb_sel) + '}\n'
                '{' + str(th_sel) + '}\n'
                '{' + str(vd_sel) + '}\n'
                '{' + str(vdc_sel) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(sol_nb) + '\n'
                '\\item ' + str(sol_th) + '\n'
                '\\item ' + str(sol_vd) + '\n'
                '\\item ' + str(sol_vdc) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

