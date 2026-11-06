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


def bt_dang15_p2_b2_c4_ds10(self):
            # Khai báo biến
            # Khởi tạo các ký hiệu
            x = symbols('x')

            # Hàm hỗ trợ định dạng số thập phân kiểu Việt Nam
            def vn_format(value, precision=2):
                return str(round(value, precision)).replace('.', ',')

            # BƯỚC 1: RANDOM DỮ LIỆU
            v0_val = random.choice([6, 7, 8])
            y0_val = random.choice([0.7, 0.8, 0.9])
            alpha_deg = random.choice([30, 45, 60])

            # Chuyển đổi sang radian
            alpha_rad = (alpha_deg * pi) / 180

            # Nội dung câu hỏi
            noidungcauhoi = (r'''Một cầu thủ bóng chuyền đón bóng bước $1$, quả bóng nảy lên và chuyển động với vận tốc ban đầu $v_0 = %s \,(m/s)$ ở độ cao $y_0 = %s \,(m)$ theo quỹ đạo là một đường Parabol. Chọn hệ trục tọa độ $Oxy$ sao cho tọa độ quả bóng ở thời điểm quả bóng bắt đầu nảy lên khỏi cánh tay của cầu thủ là $(0; y_0)$. Gọi $\alpha$ là góc hợp bởi hướng nảy lên của quả bóng so với phương ngang thì quỹ đạo chuyển động của quả bóng có phương trình là $y = \frac{-4,9x^2}{v_0^2 \cos^2 \alpha} + \tan \alpha \cdot x + y_0$.''' 
                             % (v0_val, vn_format(y0_val)))

            ########################################################################
            # Nhận biết
            ########################################################################
            he_so_mau = v0_val**2
            nb_da_1_d = r'\True Với $v_0 = %s, y_0 = %s$ phương trình quỹ đạo là $y = \frac{-4,9x^2}{%s \cos^2 \alpha} + \tan \alpha \cdot x + %s$' % (v0_val, vn_format(y0_val), he_so_mau, vn_format(y0_val))
            nb_da_1_s = r'Với $v_0 = %s, y_0 = %s$ phương trình quỹ đạo là $y = \frac{-4,9x^2}{\cos^2 \alpha} + \tan \alpha \cdot x + %s$' % (v0_val, vn_format(y0_val), vn_format(y0_val))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = r'''Thay $v_0 = %s$ và $y_0 = %s$ vào công thức $y = \frac{-4,9x^2}{v_0^2 \cos^2 \alpha} + \tan \alpha \cdot x + y_0$, ta được phương trình $y = \frac{-4,9x^2}{%s \cos^2 \alpha} + \tan \alpha \cdot x + %s$.''' % (v0_val, vn_format(y0_val), v0_val**2, vn_format(y0_val))

            ########################################################################
            # Thông hiểu
            ########################################################################
            alpha_th = 30
            h_so_a = -4.9 / (v0_val**2 * (math.cos(math.radians(alpha_th))**2))
            h_so_b = math.tan(math.radians(alpha_th))
            y_x2 = h_so_a * (2**2) + h_so_b * 2 + y0_val

            th_da_1_d = r'\True Với $\alpha = 30^\circ$, khi quả bóng chuyển động cách vị trí đón bóng $x = 2\,(m)$ thì độ cao của bóng xấp xỉ $%s\,(m)$' % vn_format(y_x2, 2)
            th_da_1_s = r'Với $\alpha = 30^\circ$, khi quả bóng chuyển động cách vị trí đón bóng $x = 2\,(m)$ thì độ cao của bóng xấp xỉ $%s\,(m)$' % vn_format(y_x2 + 1, 2)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = r'''Với $\alpha = 30^\circ$, phương trình quỹ đạo là $y = \frac{-4,9x^2}{%s \cdot \frac{3}{4}} + \frac{\sqrt{3}}{3}x + %s$. Thay $x=2$ vào phương trình, ta tính được $y \approx %s \,(m)$.''' % (v0_val**2, vn_format(y0_val), vn_format(y_x2, 2))

            ########################################################################
            # Vận dụng
            ########################################################################
            a_vd = -4.9 / (v0_val**2 * (math.cos(math.radians(60))**2))
            b_vd = math.tan(math.radians(60))
            x_max = -b_vd / (2 * a_vd)
            y_max = a_vd * (x_max**2) + b_vd * x_max + y0_val

            vd_da_1_d = r'\True Với $\alpha = 60^\circ$, quả bóng đạt độ cao lớn nhất xấp xỉ $%s\,(m)$' % vn_format(y_max, 2)
            vd_da_1_s = r'Với $\alpha = 60^\circ$, quả bóng đạt độ cao lớn nhất xấp xỉ $%s\,(m)$' % vn_format(y_max - 0.5, 2)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = r'''Với $\alpha = 60^\circ$, ta có phương trình quỹ đạo $y = %sx^2 + \sqrt{3}x + %s$. Đây là hàm số bậc hai đạt giá trị lớn nhất tại $x = \frac{-b}{2a} \approx %s$. Suy ra $y_{max} \approx %s \,(m)$.''' % (vn_format(a_vd, 2), vn_format(y0_val), vn_format(x_max, 2), vn_format(y_max, 2))

            ########################################################################
            # Vận dụng cao
            ########################################################################
            delta = b_vd**2 - 4 * a_vd * y0_val
            x_dist = (-b_vd - math.sqrt(delta)) / (2 * a_vd)
            AB = math.sqrt(y0_val**2 + x_dist**2)

            vdc_da_1_d = r'\True Với $\alpha = 60^\circ$, khoảng cách từ vị trí bóng rời tay đến vị trí chạm đất là $AB \approx %s\,(m)$' % vn_format(AB, 2)
            vdc_da_1_s = r'Với $\alpha = 60^\circ$, khoảng cách từ vị trí bóng rời tay đến vị trí chạm đất là $AB \approx %s\,(m)$' % vn_format(AB + 1.2, 2)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = r'''\begin{center} \begin{tikzpicture}[scale=0.8, font=\footnotesize, line join=round, line cap=round, >=stealth]
            \coordinate (O) at (0,0);
            \coordinate (A) at (0,1.5);
            \coordinate (B) at (4,0);
            \draw (O)--(A) node[left, midway]{$y_0$} (O)--(B) node[below, midway]{$x$} (A)--(B);
            \draw[fill=black] (O) circle (1pt) node[below left]{$O$};
            \draw[fill=black] (A) circle (1pt) node[above left]{$A$};
            \draw[fill=black] (B) circle (1pt) node[below right]{$B$};
            \end{tikzpicture} \end{center}
            Khi bóng chạm đất thì $y = 0 \Leftrightarrow %sx^2 + \sqrt{3}x + %s = 0$. Giải phương trình ta được nghiệm dương $x \approx %s\,(m)$. Vậy $OB = %s, OA = %s$. Khoảng cách $AB = \sqrt{OA^2 + OB^2} \approx %s \,(m)$.''' % (vn_format(a_vd, 2), vn_format(y0_val), vn_format(x_dist, 2), vn_format(x_dist, 2), vn_format(y0_val), vn_format(AB, 2))

            # Tổng hợp và xuất nội dung
            answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
            solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(answers[0]) + '}\n'
                '{' + str(answers[1]) + '}\n'
                '{' + str(answers[2]) + '}\n'
                '{' + str(answers[3]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(solutions[0]) + '\n'
                '\\item ' + str(solutions[1]) + '\n'
                '\\item ' + str(solutions[2]) + '\n'
                '\\item ' + str(solutions[3]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

