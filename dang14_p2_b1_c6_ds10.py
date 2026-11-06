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


def bt_dang14_p2_b1_c6_ds10(self):
            # Khai báo biến
            # Số bi xanh (nx), đỏ (nd), vàng (nv)
            nx = random.randint(3, 4)
            nd = random.randint(4, 5)
            nv = random.randint(5, 6)
            tong = nx + nd + nd
            chon = 4

            # Tính toán các giá trị tổ hợp để làm đáp án đúng
            def nCr(n, r):
                if r > n or r < 0: return 0
                return math.comb(n, r)

            # a) Không gian mẫu
            omega = nCr(nx + nd + nv, chon)

            # b) Ít nhất 1 bi xanh = Tổng - Không có bi xanh nào (chỉ chọn đỏ và vàng)
            it_nhat_1_xanh = omega - nCr(nd + nv, chon)

            # c) Đúng 1 viên bi đỏ = Chọn 1 đỏ * Chọn 3 viên còn lại (xanh hoặc vàng)
            dung_1_do = nCr(nd, 1) * nCr(nx + nv, chon - 1)

            # d) Ít nhất 2 bi đỏ = 2 đỏ + 3 đỏ + 4 đỏ
            it_nhat_2_do = (nCr(nd, 2) * nCr(nx + nv, 2) + 
                            nCr(nd, 3) * nCr(nx + nv, 1) + 
                            nCr(nd, 4) * nCr(nx + nv, 0))

            # Nội dung câu hỏi
            noidungcauhoi = ('''Trong hộp có %s bi xanh, %s bi đỏ và %s bi vàng có kích thước và khối lượng như nhau. Lấy ngẫu nhiên từ trong hộp %s viên bi.''' 
                             % (nx, nd, nv, chon))

            ########################################################################
            # Nhận biết (Câu a) ############################################
            nb_da_1_d = '\\True Số phần tử của không gian mẫu bằng %s' % (omega)
            nb_da_1_s = 'Số phần tử của không gian mẫu bằng %s' % (omega + random.choice([-5, 5, 10]))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Số phần tử của không gian mẫu là số cách chọn %s viên bi từ %s viên bi trong hộp. \\\\
                            Ta có $n\\left(\\Omega\\right) = C_{%s}^{%s} = %s$.''' 
                            % (chon, nx + nd + nv, nx + nd + nv, chon, omega))

            ########################################################################
            # Thông hiểu (Câu b) ############################################
            th_da_1_d = '\\True Số các kết quả thuận lợi cho biến cố "Trong %s viên bi được chọn có ít nhất 1 bi xanh" bằng %s' % (chon, it_nhat_1_xanh)
            th_da_1_s = 'Số các kết quả thuận lợi cho biến cố "Trong %s viên bi được chọn có ít nhất 1 bi xanh" bằng %s' % (chon, it_nhat_1_xanh - random.randint(10, 20))
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Số cách lấy %s viên bi mà không có viên bi xanh nào (chỉ lấy từ bi đỏ và vàng) là $C_{%s}^{%s} = %s$. \\\\
                            Số các kết quả thuận lợi cho biến cố có ít nhất 1 bi xanh là $%s - %s = %s$.''' 
                            % (chon, nd + nv, chon, nCr(nd + nv, chon), omega, nCr(nd + nv, chon), it_nhat_1_xanh))

            ########################################################################
            # Vận dụng (Câu c) ############################################
            vd_da_1_d = '\\True Số các kết quả thuận lợi cho biến cố "Trong %s viên bi được chọn có đúng 1 viên bi đỏ" bằng %s' % (chon, dung_1_do)
            vd_da_1_s = 'Số các kết quả thuận lợi cho biến cố "Trong %s viên bi được chọn có đúng 1 viên bi đỏ" bằng %s' % (chon, dung_1_do - 4)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Để chọn được %s viên bi có đúng 1 viên bi đỏ, ta chia làm 2 công đoạn: \\\\
                            Công đoạn 1: Chọn 1 viên bi đỏ từ %s viên bi đỏ có $C_{%s}^1$ cách. \\\\
                            Công đoạn 2: Chọn %s viên bi còn lại từ %s viên bi (xanh và vàng) có $C_{%s}^{%s}$ cách. \\\\
                            Vậy số kết quả thuận lợi là $C_{%s}^1 \\cdot C_{%s}^{%s} = %s \\cdot %s = %s$.''' 
                            % (chon, nd, nd, chon-1, nx+nv, nx+nv, chon-1, nd, nx+nv, chon-1, nCr(nd, 1), nCr(nx+nv, chon-1), dung_1_do))

            ########################################################################
            # Vận dụng cao (Câu d) ############################################
            vdc_da_1_d = '\\True Số các kết quả thuận lợi cho biến cố "Trong %s viên bi được chọn có ít nhất 2 bi đỏ" bằng %s' % (chon, it_nhat_2_do)
            vdc_da_1_s = 'Số các kết quả thuận lợi cho biến cố "Trong %s viên bi được chọn có ít nhất 2 bi đỏ" bằng %s' % (chon, it_nhat_2_do - 2)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Các trường hợp có ít nhất 2 viên bi đỏ: \\\\
                            Trường hợp 1: Có đúng 2 bi đỏ và 2 bi khác đỏ: $C_{%s}^2 \\cdot C_{%s}^2 = %s$. \\\\
                            Trường hợp 2: Có đúng 3 bi đỏ và 1 bi khác đỏ: $C_{%s}^3 \\cdot C_{%s}^1 = %s$. \\\\
                            Trường hợp 3: Có đúng 4 bi đỏ: $C_{%s}^4 = %s$. \\\\
                            Tổng số kết quả thuận lợi là $%s + %s + %s = %s$.''' 
                            % (nd, nx+nv, nCr(nd, 2)*nCr(nx+nv, 2), 
                               nd, nx+nv, nCr(nd, 3)*nCr(nx+nv, 1), 
                               nd, nCr(nd, 4), 
                               nCr(nd, 2)*nCr(nx+nv, 2), nCr(nd, 3)*nCr(nx+nv, 1), nCr(nd, 4), it_nhat_2_do))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)
                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)
                if 1 <= true_count <= 3:
                    break

            # Gán lời giải tương ứng
            loigiai_nb = loigiai_nb_1
            loigiai_th = loigiai_th_1
            loigiai_vd = loigiai_vd_1
            loigiai_vdc = loigiai_vdc_1

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(nb_da_1) + '}\n'
                '{' + str(th_da_1) + '}\n'
                '{' + str(vd_da_1) + '}\n'
                '{' + str(vdc_da_1) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb) + '\n'
                '\\item ' + str(loigiai_th) + '\n'
                '\\item ' + str(loigiai_vd) + '\n'
                '\\item ' + str(loigiai_vdc) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

