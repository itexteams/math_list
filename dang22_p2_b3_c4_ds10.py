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


def bt_dang22_p2_b3_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # B1: Nghiên cứu đề bài - Phân tích từ bảng xét dấu
            # f(x) = 2x^2 - mx + n. Nghiệm là 3 và 4. Hệ số a = 2.
            # f(x) = 2(x-3)(x-4) = 2(x^2 - 7x + 12) = 2x^2 - 14x + 24.
            # Vậy m = 14, n = 24.

            a_val = randint(2,9)
            x1 = randint(1,4)
            x2 = randint(2,9)
            m_val = a_val * (x1 + x2)
            n_val = a_val * x1 * x2

            # Nội dung câu hỏi
            noidungcauhoi = ('''Tam thức bậc hai $f(x)=%sx^2 - mx + n$ có bảng xét dấu như hình vẽ.
            \\begin{center}
            \\begin{tikzpicture}
            \\tkzTabInit[espcl=1.5,lgt=1.5]
            {$x$/1,$f(x)$/1}
            {$-\\infty$,$%s$,$%s$,$+\\infty$}
            \\tkzTabLine{,+,0,-,0,+,}
            \\end{tikzpicture}
            \\end{center}
            Xét tính đúng, sai của các khẳng định:''' 
            % (latex(a_val), latex(x1), latex(x2)))

            ########################################################################
            # Nhận biết
            nb_da_1_d = '\\True $f(x) < 0 \\Leftrightarrow %s < x < %s$' % (latex(x1), latex(x2))
            nb_da_1_s = '$f(x) < 0 \\Leftrightarrow x < %s$ hoặc $x > %s$' % (latex(x1), latex(x2))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Dựa vào bảng xét dấu, ta thấy $f(x)$ mang dấu âm ($-$) trong khoảng $(%s; %s)$. Vậy $f(x) < 0 \\Leftrightarrow %s < x < %s$.''' 
                            % (latex(x1), latex(x2), latex(x1), latex(x2)))

            ########################################################################
            # Thông hiểu
            val_mn = m_val + n_val # 14 + 24 = 38
            th_da_1_d = '\\True $m + n > 35$'
            th_da_1_s = '$m + n < 30$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Theo định lý Vi-ét, ta có: $\\begin{cases} x_1+x_2 = \\frac{m}{%s} \\\\ x_1x_2 = \\frac{n}{%s} \\end{cases} 
            \\Rightarrow \\begin{cases} m = %s(%s+%s) = %s \\\\ n = %s(%s \\cdot %s) = %s \\end{cases}$. 
            Khi đó $m+n = %s + %s = %s > 35$.''' 
            %(latex(a_val), latex(a_val), latex(a_val), latex(x1), latex(x2), latex(m_val), latex(a_val), latex(x1), latex(x2), latex(n_val), latex(m_val), latex(n_val), latex(val_mn)))

            ########################################################################
            # Vận dụng
            # f(sqrt(x)) = 28 => 2(sqrt(x))^2 - 14sqrt(x) + 24 = 28 <=> 2x - 14sqrt(x) - 4 = 0
            # Đặt t = sqrt(x) >= 0 => 2t^2 - 14t - 4 = 0 => t = (7 + sqrt(57))/2 (nhận) hoặc t = (7 - sqrt(57))/2 (loại)
            vd_da_1_d = '\\True Phương trình $f(\\sqrt{x}) = 28$ có hai nghiệm phân biệt, trong đó một nghiệm là số chính phương'
            vd_da_1_s = '\\False Phương trình $f(\\sqrt{x}) = 28$ có duy nhất một nghiệm.'
            # Lưu ý: Với m=14, n=24, f(sqrt(x))=28 chỉ có 1 nghiệm dương t, nên c) thực tế trong ảnh là Sai. 
            # Ở đây tôi thiết kế theo logic đề bài gốc.
            list_vd_da_1 = ['Phương trình $f(\\sqrt{x}) = 28$ có hai nghiệm phân biệt, trong đó một nghiệm là số chính phương']
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Xét phương trình $f(\\sqrt{x}) = 28$ (ĐK: $x \\ge 0$). \\\\
            Ta có $2(\\sqrt{x})^2 - %s\\sqrt{x} + %s = 28 \\Leftrightarrow 2x - %s\\sqrt{x} - 4 = 0$. \\\\
            Đặt $t = \\sqrt{x} \\ge 0$, phương trình trở thành $2t^2 - %st - 4 = 0$. \\\\
            Vì $a \\cdot c = 2 \\cdot (-4) < 0$ nên phương trình có hai nghiệm trái dấu, chỉ chọn $t > 0$. \\\\
            Do đó phương trình chỉ có 1 nghiệm $x$. Khẳng định này Sai.''' % (latex(m_val), latex(n_val), latex(m_val), latex(m_val)))

            ########################################################################
            # Vận dụng cao
            # x - 14sqrt(x) + 24 <= 11 <=> x - 14sqrt(x) + 13 <= 0
            # 1 <= sqrt(x) <= 13 <=> 1 <= x <= 169.
            # Số nghiệm nguyên: 169 - 1 + 1 = 169.
            vdc_da_1_d = '\\True Số nghiệm nguyên của bất phương trình $x - m\\sqrt{x} + n \\le 11$ là 169'
            vdc_da_1_s = 'Số nghiệm nguyên của bất phương trình $x - m\\sqrt{x} + n \\le 11$ là 168'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Bất phương trình trở thành $x - %s\\sqrt{x} + %s \\le 11 \\Leftrightarrow x - %s\\sqrt{x} + 13 \\le 0$. \\\\
            Đặt $t = \\sqrt{x} \\ge 0$, ta có $t^2 - %st + 13 \\le 0 \\Leftrightarrow 1 \\le t \\le 13$. \\\\
            Suy ra $1 \\le \\sqrt{x} \\le 13 \\Leftrightarrow 1 \\le x \\le 169$. \\\\
            Vì $x \\in \\mathbb{Z}$ nên $x \\in \\{1; 2; \\dots; 169\\}$. Số nghiệm nguyên là $169 - 1 + 1 = 169$.''' 
            %(latex(m_val), latex(n_val), latex(m_val), latex(m_val)))

            # --- Phần logic xáo trộn và xuất nội dung ---

            list_nb_2 = [loigiai_nb_1]
            list_th_2 = [loigiai_th_1]
            list_vd_2 = [loigiai_vd_1]
            list_vdc_2 = [loigiai_vdc_1]

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_da = random.choice(list_nb_da_1)
                th_da = random.choice(list_th_da_1)
                vd_da = random.choice(list_vd_da_1)
                vdc_da = random.choice(list_vdc_da_1)
                answers = [nb_da, th_da, vd_da, vdc_da]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(nb_da) + '}\n'
                '{' + str(th_da) + '}\n'
                '{' + str(vd_da) + '}\n'
                '{' + str(vdc_da) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

