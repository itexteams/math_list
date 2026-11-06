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


def bt_dang12_p1_b1_c1_hh11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # 1. Định nghĩa các trường hợp tìm giao tuyến
                dinh_chinh = 'S'
                giao_diem_phu = 'O'

                # Danh sách các cặp mặt phẳng và giao tuyến tương ứng
                cac_giao_tuyen = [
                    {
                        'mp1': f'({dinh_chinh}AC)',
                        'mp2': f'({dinh_chinh}BD)',
                        'giao_tuyen': f'{dinh_chinh}{giao_diem_phu}', # SO
                        'diem_chung_1': dinh_chinh,
                        'diem_chung_2_text': f'{giao_diem_phu} (là giao điểm của AC và BD)'
                    },
                    {
                        'mp1': f'({dinh_chinh}AB)',
                        'mp2': f'({dinh_chinh}AD)',
                        'giao_tuyen': f'{dinh_chinh}A', # SA
                        'diem_chung_1': dinh_chinh,
                        'diem_chung_2_text': f'A (là điểm chung của AB và AD)'
                    },
                    {
                        'mp1': f'({dinh_chinh}BC)',
                        'mp2': f'({dinh_chinh}CD)',
                        'giao_tuyen': f'{dinh_chinh}C', # SC
                        'diem_chung_1': dinh_chinh,
                        'diem_chung_2_text': f'C (là điểm chung của BC và CD)'
                    },
                    {
                        'mp1': f'({dinh_chinh}AB)',
                        'mp2': f'({dinh_chinh}BC)',
                        'giao_tuyen': f'{dinh_chinh}B', # SB
                        'diem_chung_1': dinh_chinh,
                        'diem_chung_2_text': f'B (là điểm chung của AB và BC)'
                    }
                ]

                # 2. Chọn ngẫu nhiên một trường hợp
                case = random.choice(cac_giao_tuyen)
                mp1 = case['mp1']
                mp2 = case['mp2']
                giao_tuyen_dung = case['giao_tuyen']
                diem_chung_1 = case['diem_chung_1']
                diem_chung_2_text = case['diem_chung_2_text']

                # Câu hỏi
                # Chỉ hỏi về giao tuyến, không nhắc đến O nếu không dùng
                if giao_tuyen_dung == f'{dinh_chinh}{giao_diem_phu}':
                    noidungcauhoi = ('''Cho hình chóp $S.ABCD$. Gọi $O$ là giao điểm của $AC$ và $BD$. Giao tuyến của hai mặt phẳng $%s$ và $%s$ là'''
                                  %(mp1, mp2))
                else:
                     noidungcauhoi = ('''Cho hình chóp $S.ABCD$. Gọi $O$ là giao điểm của $AC$ và $BD$. Giao tuyến của hai mặt phẳng $%s$ và $%s$ là'''
                                  %(mp1, mp2))

                # Đáp án đúng
                da_d = ('\\True ' + f'Đường thẳng ${giao_tuyen_dung}$')

                # 3. Tạo các đáp án nhiễu (DAS)
                # Lấy các giao tuyến khác (SA, SB, SC, SD, SO,...) làm đáp án nhiễu

                giao_tuyen_nguoc = {item['giao_tuyen'] for item in cac_giao_tuyen if item['giao_tuyen'] != giao_tuyen_dung}

                # Thêm các đường chéo đáy và cạnh bên làm nhiễu
                s = list(giao_tuyen_nguoc)
                s.extend(['AC', 'BD', 'AB', 'CD', 'AD', 'BC'])

                # Format đáp án nhiễu
                s = [f'Đường thẳng ${item}$' for item in s]
                s.append(f'Điểm ${diem_chung_1}$') # Nhiễu: Chỉ là 1 điểm chung
                s.append(f'Đường thẳng $O{diem_chung_1}$')

                # Chọn 3 đáp án sai ngẫu nhiên
                random.shuffle(s)

                # Đảm bảo 3 đáp án được chọn không trùng lặp
                das1 = s.pop(0)
                das2 = s.pop(0)
                das3 = s.pop(0)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai=('''Ta tìm hai điểm chung của hai mặt phẳng $%s$ và $%s$:\\\\
                         Hai mặt phẳng đều chứa đỉnh $%s$ (theo tên gọi của hình chóp), nên $%s$ là điểm chung thứ nhất.\\\\
                         Điểm chung thứ hai chính là %s.\\\\
                         Giao tuyến của hai mặt phẳng này là đường thẳng đi qua hai điểm chung đó, tức là Đường thẳng $%s$.'''
                          %(mp1, mp2, diem_chung_1, diem_chung_1, diem_chung_2_text, giao_tuyen_dung))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

