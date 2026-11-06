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


def bt_dang10_p2_b3_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # B1 & B3: Thiết lập thông số bài toán và Random
            # Chu vi tấm sắt P = 96. Cạnh hình vuông cắt đi c = 4.
            # Ta có thể random chu vi P là số chẵn (ví dụ từ 80 đến 120) và cạnh c (từ 2 đến 5)
            P = 96 
            c = 4
            nua_chu_vi = P // 2 # 48

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một tấm sắt hình chữ nhật có chu vi là %s cm. Người ta cắt ở mỗi góc tấm sắt một hình vuông cạnh là %s cm.''' 
                             %(latex(P), latex(c)))

            ########################################################################
            # a) Nhận biết: Diện tích phần cắt đi
            S_cat_dung = 4 * (c**2)
            S_cat_sai = c**2
            nb_da_1_d = '\\True Diện tích phần cắt đi là %s (cm$^2$)' %(latex(S_cat_dung))
            nb_da_1_s = 'Diện tích phần cắt đi là %s (cm$^2$)' %(latex(S_cat_sai))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Vì cắt ở mỗi góc một hình vuông cạnh là %s cm nên có tất cả 4 hình vuông được cắt đi. \\\\ Diện tích phần cắt đi là: $4 \\times %s^2 = %s$ (cm$^2$).''' 
                            %(latex(c), latex(c), latex(S_cat_dung)))

            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # b) Thông hiểu: Mối quan hệ giữa chiều dài và chiều rộng
            th_da_1_d = '\\True Gọi chiều dài của tấm sắt là $x$ (cm) thì chiều rộng tấm sắt là %s - $x$ (cm)' %(latex(nua_chu_vi))
            th_da_1_s = 'Gọi chiều dài của tấm sắt là $x$ (cm) thì chiều rộng tấm sắt là %s - $x$ (cm)' %(latex(P))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Nửa chu vi của tấm sắt hình chữ nhật là: $%s : 2 = %s$ (cm). \\\\ Nếu gọi chiều dài là $x$ (cm) thì chiều rộng là $%s - x$ (cm).''' 
                            %(latex(P), latex(nua_chu_vi), latex(nua_chu_vi)))

            list_th_2 = [loigiai_th_1]

            ########################################################################
            # c) Vận dụng: Biểu thức diện tích phần còn lại
            # S_con_lai = x*(nua_chu_vi - x) - 4*c^2 = -x^2 + nua_chu_vi*x - 4*c^2
            S_con_lai_bieuthuc = -x**2 + nua_chu_vi*x - S_cat_dung
            vd_da_1_d = '\\True Diện tích phần còn lại của tấm sắt là $%s$ (cm$^2$)' %(latex(S_con_lai_bieuthuc))
            vd_da_1_s = 'Diện tích phần còn lại của tấm sắt là $-x^2 + %s x$ (cm$^2$)' %(latex(nua_chu_vi))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Diện tích ban đầu của tấm sắt là: $x(%s - x) = -x^2 + %s x$ (cm$^2$). \\\\ Diện tích phần còn lại sau khi cắt là diện tích ban đầu trừ đi diện tích 4 hình vuông góc: \\\\ $S = (-x^2 + %s x) - %s = %s$ (cm$^2$).''' 
                            %(latex(nua_chu_vi), latex(nua_chu_vi), latex(nua_chu_vi), latex(S_cat_dung), latex(S_con_lai_bieuthuc)))

            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # d) Vận dụng cao: Bất phương trình diện tích
            # S >= 448 <=> -x^2 + 48x - 64 >= 448 <=> -x^2 + 48x - 512 >= 0
            # Nghiệm của -x^2 + 48x - 512 = 0 là x = 16 và x = 32.
            S_nguong = 448
            vdc_da_1_d = '\\True Diện tích phần còn lại của tấm sắt ít nhất bằng %s cm$^2$ khi và chỉ khi chiều dài của tấm sắt nằm trong đoạn $[16; 32]$' %(latex(S_nguong))
            vdc_da_1_s = 'Diện tích phần còn lại của tấm sắt ít nhất bằng %s cm$^2$ khi và chỉ khi chiều dài của tấm sắt nằm trong đoạn $[10; 38]$' %(latex(S_nguong))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Để diện tích còn lại ít nhất bằng %s cm$^2$, ta có bất phương trình: \\\\ $%s \\ge %s \\Leftrightarrow -x^2 + %s x - %s \\ge 0 \\Leftrightarrow (x - 16)(32 - x) \\ge 0$. \\\\ Giải bất phương trình ta được $16 \\le x \\le 32$. \\\\ Vậy chiều dài tấm sắt nằm trong đoạn $[16; 32]$.''' 
                             %(latex(S_nguong), latex(S_con_lai_bieuthuc), latex(S_nguong), latex(nua_chu_vi), latex(S_nguong + S_cat_dung)))

            list_vdc_2 = [loigiai_vdc_1]

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                ans_a = random.choice(list_nb_da_1)
                ans_b = random.choice(list_th_da_1)
                ans_c = random.choice(list_vd_da_1)
                ans_d = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([ans_a, ans_b, ans_c, ans_d]) <= 3:
                    break

            # Hình vẽ TikZ
            hinh_ve = ('''\\begin{center}
            \\begin{tikzpicture}[scale=0.8]
                \\draw[thick, blue] (0,0) rectangle (6,3);
                \\fill[black] (0,0) rectangle (0.8,0.8);
                \\fill[black] (5.2,0) rectangle (6,0.8);
                \\fill[black] (0,2.2) rectangle (0.8,3);
                \\fill[black] (5.2,2.2) rectangle (6,3);
                \\draw (0.8,0) -- (0.8,3);
                \\draw (5.2,0) -- (5.2,3);
                \\draw (0,0.8) -- (6,0.8);
                \\draw (0,2.2) -- (6,2.2);
            \\end{tikzpicture}
            \\end{center}''')

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n' +
                str(hinh_ve) + '\n' +
                '\\choiceTFn \n'
                '{' + str(ans_a) + '}\n'
                '{' + str(ans_b) + '}\n'
                '{' + str(ans_c) + '}\n'
                '{' + str(ans_d) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

