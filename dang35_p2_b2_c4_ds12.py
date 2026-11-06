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


def bt_dang35_p2_b2_c4_ds12(self):
            # Khai báo biến
            # Hàm hỗ trợ định dạng số thập phân dùng dấu phẩy
            def f_dec(val):
                return str(round(float(val), 2)).replace('.', ',')

            # 1. Khởi tạo và ngẫu nhiên hóa các giá trị cơ bản
            # P(A): Xác suất bị tiểu đường (40% -> 0,4)
            pA_val = random.choice([0.3, 0.35, 0.4, 0.45, 0.5])
            # P(B|A): Xác suất bị huyết áp cao khi đã bị tiểu đường (70% -> 0,7)
            pB_cond_A_val = random.choice([0.6, 0.65, 0.7, 0.75, 0.8])
            # P(B|notA): Xác suất bị huyết áp cao khi không bị tiểu đường (25% -> 0,25)
            pB_cond_notA_val = random.choice([0.15, 0.2, 0.25, 0.3])

            # Các giá trị tính toán
            p_notA_val = 1 - pA_val
            pB_val = pA_val * pB_cond_A_val + p_notA_val * pB_cond_notA_val

            # Nội dung câu hỏi gốc
            noidungcauhoi = ('''Khi điều tra sức khỏe nhiều người cao tuổi ở một địa phương, người ta thấy rằng có %s\\%% người cao tuổi bị bệnh tiểu đường. Bên cạnh đó, số người bị bệnh huyết áp cao trong số những người bị bệnh tiểu đường là %s\\%%, trong những người không bị bệnh tiểu đường là %s\\%%. Chọn ngẫu nhiên một người cao tuổi để kiểm tra sức khỏe.''' 
                             %(int(pA_val*100), int(pB_cond_A_val*100), int(pB_cond_notA_val*100)))

            ########################################################################
            # Nhận biết - Câu a: Xác suất bị tiểu đường
            ########################################################################
            nb_da_1_d = '\\True Xác suất chọn được người bị bệnh tiểu đường là %s' % f_dec(pA_val)
            nb_da_1_s = 'Xác suất chọn được người bị bệnh tiểu đường là %s' % f_dec(pA_val + 0.1)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Gọi $A$ là biến cố "Chọn được người cao tuổi bị tiểu đường". Khi đó $P(A)=%s$.''' % f_dec(pA_val))

            ########################################################################
            # Thông hiểu - Câu b: Xác suất có điều kiện P(B|A)
            ########################################################################
            th_da_1_d = '\\True Xác suất chọn được người bị bệnh huyết áp cao, biết người đó bị bệnh tiểu đường là %s' % f_dec(pB_cond_A_val)
            th_da_1_s = 'Xác suất chọn được người bị bệnh huyết áp cao, biết người đó bị bệnh tiểu đường là %s' % f_dec(pB_cond_A_val - 0.05)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Gọi $B$ là biến cố "Chọn được người cao tuổi bị huyết áp cao". Theo giả thiết ta có $P(B|A)=%s$.''' % f_dec(pB_cond_A_val))

            ########################################################################
            # Vận dụng - Câu c: Xác suất có điều kiện P(B|notA)
            ########################################################################
            vd_da_1_d = '\\True Xác suất chọn được người bị bệnh huyết áp cao, biết người đó không bị bệnh tiểu đường là %s' % f_dec(pB_cond_notA_val)
            vd_da_1_s = 'Xác suất chọn được người bị bệnh huyết áp cao, biết người đó không bị bệnh tiểu đường là %s' % f_dec(1 - pB_cond_notA_val)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Xác suất chọn được người bị bệnh huyết áp cao, biết người đó không bị bệnh tiểu đường là $P(B|\\bar{A})=%s$.''' % f_dec(pB_cond_notA_val))

            ########################################################################
            # Vận dụng cao - Câu d: Công thức xác suất toàn phần P(B)
            ########################################################################
            vdc_da_1_d = '\\True Xác suất chọn được người bị bệnh huyết áp cao là %s' % f_dec(pB_val)
            vdc_da_1_s = 'Xác suất chọn được người bị bệnh huyết áp cao là %s' % f_dec(pB_val + 0.02)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Ta có $P(A)=%s \\Rightarrow P(\\bar{A})=1-%s=%s$. \\\\ Theo công thức xác suất toàn phần ta có: \\\\ $P(B)=P(A).P(B|A)+P(\\bar{A}).P(B|\\bar{A})=%s.%s+%s.%s=%s$.''' 
                             % (f_dec(pA_val), f_dec(pA_val), f_dec(p_notA_val), f_dec(pA_val), f_dec(pB_cond_A_val), f_dec(p_notA_val), f_dec(pB_cond_notA_val), f_dec(pB_val)))

            # --- Logic xáo trộn và chọn số lượng đáp án đúng (từ 1 đến 3) ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                ans_a = random.choice(list_nb_da_1)
                ans_b = random.choice(list_th_da_1)
                ans_c = random.choice(list_vd_da_1)
                ans_d = random.choice(list_vdc_da_1)

                current_answers = [ans_a, ans_b, ans_c, ans_d]
                if 1 <= count_true_answers(current_answers) <= 3:
                    break

            # Xuất nội dung theo cấu trúc yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
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

