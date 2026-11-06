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


def bt_dang37_p3_b1_c5_ds10(self):
            # Khai báo biến
            # Khai báo các biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Random số chữ số n (chọn n chẵn để giữ logic vị trí lẻ/chẵn bằng nhau)
                n = random.choice([8, 10, 12, 14])
                k = n // 2 

                # Tính toán kết quả: 2 * (2^k)
                # Sửa lỗi cú pháp: đặt tên biến viết liền
                kq_giatri = 2 * (2**k)

                # Bước 4: Tạo các phương án sai không trùng đáp án đúng
                s_options = set()
                while len(s_options) < 3:
                    sai = random.choice([
                        2**k, 
                        2**(k + 2), 
                        kq_giatri + 10, 
                        kq_giatri - 10, 
                        80, 32, 16, 64
                    ])
                    if sai != kq_giatri and sai > 0:
                        s_options.add('$%s$' % (latex(sai)))

                list_sai = list(s_options)
                das1, das2, das3 = list_sai[0], list_sai[1], list_sai[2]
                da_dung = '$%s$' % (latex(kq_giatri))

                # Câu hỏi
                noidungcauhoi = ('''Có bao nhiêu số có $%s$ chữ số được tạo thành từ các chữ số $1, 2, 3$ sao cho bất kì $2$ chữ số nào đứng cạnh nhau cũng hơn kém nhau $1$ đơn vị?'''
                                 % (latex(n)))

                # Các đáp án
                da_d = ('\\True ' + str(da_dung))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Trộn đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết (Sử dụng \\left( và \\right))
                loigiai = ('''Gọi số tự nhiên cần tìm có dạng $\\overline{a_1a_2a_3\\dots a_{%s}}$.\\\\
                           Bước 1: Xếp số $2$ ở vị trí lẻ $a_1, a_3, \\dots, a_{%s}$ hoặc vị trí chẵn $a_2, a_4, \\dots, a_{%s}$ có $2$ cách.\\\\
                           Bước 2: Xếp các số $1$ hoặc $3$ vào các vị trí còn lại có $2^{%s}$ cách.\\\\
                           Theo quy tắc nhân ta có $2 \\cdot 2^{%s} = %s$ cách.'''
                           % (latex(n), latex(n-1), latex(n), latex(k), latex(k), latex(kq_giatri)))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq_giatri))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

