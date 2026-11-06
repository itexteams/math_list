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


def bt_dang56_p4_b2_c6_ds10(self):
            #Khai báo biến
            # Khai báo biến loại bài tập
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Suy nghĩ tìm cách random bài toán
                # Chọn ngẫu nhiên số lượng nam và nữ để bài toán phong phú
                nam = random.randint(18, 25)
                nu = random.randint(12, 17)
                tong = nam + nu
                k = 4 # Số học sinh được chọn

                # Bước 1 & 2: Nghiên cứu và viết lại logic bài toán
                # Tính số phần tử không gian mẫu
                n_omega = int(binomial(tong, k))

                # Tính số cách chọn 4 nam
                n_nam = int(binomial(nam, k))

                # Tính số cách chọn 4 nữ
                n_nu = int(binomial(nu, k))

                # Số cách chọn có cả nam và nữ (biến cố đối)
                n_A = n_omega - n_nam - n_nu

                # Xác suất (dạng phân số tối giản)
                p_xacsuat = Rational(n_A, n_omega)
                p_tu = p_xacsuat.p # Tử số tối giản
                p_mau = p_xacsuat.q # Mẫu số tối giản

                # Tạo đáp án đúng
                da = '$P = \\frac{%s}{%s}$' % (latex(p_tu), latex(p_mau))

                # Bước 4: Điều chỉnh các phương án sai (không trùng đáp án đúng)
                s = []
                # Phương án sai 1: Thay đổi tử số một chút
                s1 = '$P = \\frac{%s}{%s}$' % (latex(p_tu - 5), latex(p_mau))
                # Phương án sai 2: Hoán đổi vị trí chữ số ở mẫu
                mau_str = str(p_mau)
                if len(mau_str) >= 4:
                    mau_sai = mau_str[:-2] + mau_str[-1] + mau_str[-2]
                else:
                    mau_sai = str(p_mau + 27)
                s2 = '$P = \\frac{%s}{%s}$' % (latex(p_tu), mau_sai)

                # Phương án sai 3: Hoán đổi vị trí chữ số ở tử
                tu_str = str(p_tu)
                if len(tu_str) >= 4:
                    tu_sai = tu_str[:-2] + tu_str[-1] + tu_str[-2]
                else:
                    tu_sai = str(p_tu + 36)
                s3 = '$P = \\frac{%s}{%s}$' % (tu_sai, latex(p_mau))

                # Danh sách các phương án sai
                list_sai = [s1, s2, s3]

                # Câu hỏi
                noidungcauhoi = ('''Một lớp có $%s$ nam và $%s$ nữ. Giáo viên chọn ngẫu nhiên $%s$ học sinh lên bảng giải bài tập. Tính xác suất $P$ để $%s$ học sinh được chọn có cả nam và nữ.'''
                                 % (latex(nam), latex(nu), latex(k), latex(k)))

                # Các đáp án trắc nghiệm
                da_d = ('\\True ' + str(da))
                da_s1 = str(list_sai[0])
                da_s2 = str(list_sai[1])
                da_s3 = str(list_sai[2])

                # Đưa các đáp án vào danh sách và xáo trộn
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết (không viết tắt)
                loigiai = ('''Số học sinh của lớp là : $%s + %s = %s$. \\\\
            Số cách chọn $%s$ học sinh trong lớp là : $n\\left(\\Omega\\right) = C_{%s}^{%s} = %s$. \\\\
            Số cách chọn $%s$ học sinh nam trong lớp là : $C_{%s}^{%s} = %s$. \\\\
            Số cách chọn $%s$ học sinh nữ trong lớp là : $C_{%s}^{%s} = %s$. \\\\
            Số cách chọn $%s$ học sinh có cả nam và nữ là : $%s - %s - %s = %s$. \\\\
            Vậy xác suất cần tìm là $P = \\frac{%s}{%s} = \\frac{%s}{%s}$.'''
                           % (latex(nam), latex(nu), latex(tong),
                              latex(k), latex(tong), latex(k), latex(n_omega),
                              latex(k), latex(nam), latex(k), latex(n_nam),
                              latex(k), latex(nu), latex(k), latex(n_nu),
                              latex(k), latex(n_omega), latex(n_nam), latex(n_nu), latex(n_A),
                              latex(n_A), latex(n_omega), latex(p_tu), latex(p_mau)))

            # Xuất nội dung theo định dạng yêu cầu (không dùng tiền tố r)
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 

