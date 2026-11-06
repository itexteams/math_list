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


def bt_dang12_p2_b2_c5_ds10(self):
            # Khai báo biến
            # Hàm tính tổ hợp
            def nCr(n, r):
                if r < 0 or r > n:
                    return 0
                return math.comb(n, r)

            # B1: Nghiên cứu đề bài và random số liệu
            # Random số lượng bi mỗi loại
            nx = random.randint(5, 8)  # Số bi xanh
            nd = random.randint(4, 6)  # Số bi đỏ
            nv = random.randint(3, 5)  # Số bi vàng

            # Tính toán các giá trị đúng
            val_a = nCr(nx, 2) * nCr(nd, 1) * nCr(nv, 1)
            val_b = nCr(nx, 1) * nCr(nd, 2) * nCr(nv, 1)
            val_c = nCr(nx, 1) * nCr(nd, 1) * nCr(nv, 2)
            val_d = val_a + val_b + val_c

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một hộp có %s viên bi xanh, %s viên bi đỏ và %s viên bi vàng, chọn ngẫu nhiên 4 viên bi.''' 
                             %(latex(nx), latex(nd), latex(nv)))

            ########################################################################
            # Nhận biết (Câu a)
            sa_a_d = '\\True Chọn 2 bi xanh, 1 bi đỏ và 1 bi vàng có: %s cách' %(latex(val_a))
            sa_a_s = 'Chọn 2 bi xanh, 1 bi đỏ và 1 bi vàng có: %s cách' %(latex(val_a + random.choice([-20, 20, 50])))
            list_nb_da_1 = [sa_a_d, sa_a_s]

            loigiai_nb_1 = ('''Số cách chọn 2 bi xanh, 1 bi đỏ và 1 bi vàng là $C_{%s}^2 \\cdot C_{%s}^1 \\cdot C_{%s}^1 = %s$ cách.'''
                            %(latex(nx), latex(nd), latex(nv), latex(val_a)))

            ########################################################################
            # Thông hiểu (Câu b)
            sa_b_d = '\\True Chọn 1 bi xanh, 2 bi đỏ và 1 bi vàng có: %s cách' %(latex(val_b))
            sa_b_s = 'Chọn 1 bi xanh, 2 bi đỏ và 1 bi vàng có: %s cách' %(latex(val_b + random.choice([-10, 10, 30])))
            list_th_da_1 = [sa_b_d, sa_b_s]

            loigiai_th_1 = ('''Số cách chọn 1 bi xanh, 2 bi đỏ và 1 bi vàng là $C_{%s}^1 \\cdot C_{%s}^2 \\cdot C_{%s}^1 = %s$ cách.'''
                            %(latex(nx), latex(nd), latex(nv), latex(val_b)))

            ########################################################################
            # Vận dụng (Câu c)
            sa_c_d = '\\True Chọn 1 bi xanh, 1 bi đỏ và 2 bi vàng có: %s cách' %(latex(val_c))
            sa_c_s = 'Chọn 1 bi xanh, 1 bi đỏ và 2 bi vàng có: %s cách' %(latex(val_c + random.choice([-15, 15, 40])))
            list_vd_da_1 = [sa_c_d, sa_c_s]

            loigiai_vd_1 = ('''Số cách chọn 1 bi xanh, 1 bi đỏ và 2 bi vàng là $C_{%s}^1 \\cdot C_{%s}^1 \\cdot C_{%s}^2 = %s$ cách.'''
                            %(latex(nx), latex(nd), latex(nv), latex(val_c)))

            ########################################################################
            # Vận dụng cao (Câu d)
            sa_d_d = '\\True Có %s cách chọn ngẫu nhiên 4 viên bi từ hộp sao cho có đủ cả ba màu' %(latex(val_d))
            sa_d_s = 'Có %s cách chọn ngẫu nhiên 4 viên bi từ hộp sao cho có đủ cả ba màu' %(latex(val_d - random.choice([50, 100, 120])))
            list_vdc_da_1 = [sa_d_d, sa_d_s]

            loigiai_vdc_1 = ('''Để chọn 4 viên bi có đủ 3 màu, ta có các trường hợp sau: \\\\
            - TH1: 2 xanh, 1 đỏ, 1 vàng: $C_{%s}^2 \\cdot C_{%s}^1 \\cdot C_{%s}^1 = %s$. \\\\
            - TH2: 1 xanh, 2 đỏ, 1 vàng: $C_{%s}^1 \\cdot C_{%s}^2 \\cdot C_{%s}^1 = %s$. \\\\
            - TH3: 1 xanh, 1 đỏ, 2 vàng: $C_{%s}^1 \\cdot C_{%s}^1 \\cdot C_{%s}^2 = %s$. \\\\
            Tổng số cách chọn là: $%s + %s + %s = %s$.'''
                            %(latex(nx), latex(nd), latex(nv), latex(val_a),
                              latex(nx), latex(nd), latex(nv), latex(val_b),
                              latex(nx), latex(nd), latex(nv), latex(val_c),
                              latex(val_a), latex(val_b), latex(val_c), latex(val_d)))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp để đảm bảo có từ 1 đến 3 câu đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lời giải tương ứng (trong bài này lời giải là cố định cho từng ý)
            list_nb_2 = [loigiai_nb_1]
            list_th_2 = [loigiai_th_1]
            list_vd_2 = [loigiai_vd_1]
            list_vdc_2 = [loigiai_vdc_1]

            # Xuất câu hỏi
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\\choiceTFn \n'
                '{'+str(nb_da_1)+'}\n'
                '{'+str(th_da_1)+'}\n'
                '{'+str(vd_da_1)+'}\n'
                '{'+str(vdc_da_1)+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(loigiai_nb_1)+'\n'
                '\\item '+str(loigiai_th_1)+'\n'
                '\\item '+str(loigiai_vd_1)+'\n'
                '\\item '+str(loigiai_vdc_1)+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

