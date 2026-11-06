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


def bt_dang14_p1_b2_c6_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Số mặt của xúc xắc
                n = 6
                n_le = 3
                n_chan = 3

                # Không gian mẫu
                kgm = n * n

                # Random yêu cầu: tích là số chẵn hoặc tích là số lẻ
                loai_bien_co = random.choice(['chẵn', 'lẻ'])

                if loai_bien_co == 'chẵn':
                    # Trường hợp 1: Lần 1 lẻ (3), lần 2 chẵn (3) -> 3*3 = 9
                    th1 = n_le * n_chan
                    # Trường hợp 2: Lần 1 chẵn (3), lần 2 bất kỳ (6) -> 3*6 = 18
                    th2 = n_chan * n
                    fav = th1 + th2
                    text_bc = "một số chẵn"
                    # Chi tiết lời giải cho loại chẵn
                    chi_tiet_lg = ('''Ta xét các trường hợp: \\\\
                             \\textbf{TH1:} Gieo lần một số chấm xuất hiện trên mặt là số lẻ thì khi gieo lần hai, số chấm xuất hiện phải là số chẵn. Khi đó có $%s \\cdot %s = %s$ cách gieo. \\\\
                             \\textbf{TH2:} Gieo lần một số chấm xuất hiện trên mặt là số chẵn thì khi gieo lần hai, số chấm xuất hiện có thể là số chẵn hoặc số lẻ. Khi đó có $%s \\cdot %s = %s$ cách gieo.''' 
                             %(latex(n_le), latex(n_chan), latex(th1), latex(n_chan), latex(n), latex(th2)))
                else:
                    # Tích là số lẻ khi và chỉ khi cả 2 lần đều lẻ
                    fav = n_le * n_le
                    text_bc = "một số lẻ"
                    chi_tiet_lg = ("Để tích hai lần gieo là một số lẻ thì cả hai lần gieo đều phải xuất hiện mặt có số chấm là số lẻ. \\\\ Khi đó có $%s \\cdot %s = %s$ cách gieo." 
                                   %(latex(n_le), latex(n_le), latex(fav)))

                # Tính xác suất
                xs = Rational(fav, kgm)
                kq_val = float(xs)
                # Định dạng dấu phẩy cho số thập phân
                kq_str = str(Decimal(str(kq_val)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')

                # Đáp án đúng
                da = '$%s$' % (kq_str)

                # Tạo các đáp án sai không trùng đáp án đúng
                list_fake = [0.25, 0.5, 0.75, 0.85, 0.15, 0.35, 0.45]
                s = []
                for v in list_fake:
                    val_str = str(Decimal(str(v)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')
                    if val_str != kq_str:
                        s.append('$%s$' % val_str)

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Gieo một con xúc xắc cân đối đồng chất hai lần. Xác suất để biến cố có tích hai lần số chấm khi gieo xúc xắc là %s bằng'''
                                 % (text_bc))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Số phần tử của không gian mẫu là $n(\\Omega)= %s \\cdot %s = %s$. \\\\
                             Gọi $A$ là biến cố '%s'. \\\\
                             %s \\\\
                             Suy ra số kết quả thuận lợi cho biến cố là $n(A) = %s$. \\\\
                             Vậy xác suất cần tính $P\\left(A\\right) = \\frac{%s}{%s} = %s$.'''
                           %(latex(n), latex(n), latex(kgm), 
                             noidungcauhoi.split('biến cố có ')[1].replace(' bằng', ''),
                             chi_tiet_lg,
                             latex(fav),
                             latex(fav), latex(kgm), kq_str
                           ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ ' \n'
                '\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

