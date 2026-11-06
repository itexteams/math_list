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


def bt_dang14_p1_b2_c1_hh12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Hàm hỗ trợ định dạng số âm cho vào trong ngoặc đơn để công thức đẹp hơn
                def fm(val):
                    return f"({val})" if val < 0 else str(val)

                # Vòng lặp đảm bảo sinh số liệu hợp lệ và 4 đáp án hoàn toàn phân biệt
                while True:
                    # 1. Sinh ngẫu nhiên tọa độ điểm A
                    xA, yA, zA = randint(-5, 5), randint(-5, 5), randint(-5, 5)

                    # 2. Sinh ngẫu nhiên độ lệch để tạo điểm B
                    # Nhân 2 độ lệch để đảm bảo tính chẵn lẻ của xB giống xA, 
                    # giúp đáp án nhiễu "tọa độ trung điểm" luôn là số nguyên.
                    dx, dy, dz = randint(-4, 4), randint(-4, 4), randint(-4, 4)
                    if dx == 0 and dy == 0 and dz == 0:
                        continue

                    xB, yB, zB = xA + 2*dx, yA + 2*dy, zA + 2*dz

                    # 3. Tính toán các đáp án
                    # Đáp án đúng: vector AB = B - A
                    ans_correct = (xB - xA, yB - yA, zB - zA)

                    # Nhiễu 1: Tính ngược thành vector BA = A - B
                    ans_w1 = (xA - xB, yA - yB, zA - zB)

                    # Nhiễu 2: Cộng nhầm tọa độ A + B
                    ans_w2 = (xA + xB, yA + yB, zA + zB)

                    # Nhiễu 3: Tính nhầm sang tọa độ trung điểm đoạn AB
                    ans_w3 = ((xA + xB)//2, (yA + yB)//2, (zA + zB)//2)

                    # Kiểm tra tính duy nhất của các đáp án, nếu có trùng lặp thì sinh lại
                    opts = {ans_correct, ans_w1, ans_w2, ans_w3}
                    if len(opts) == 4:
                        break

                # 4. Định dạng chuỗi hiển thị
                da = f"$({ans_correct[0]}; {ans_correct[1]}; {ans_correct[2]})$"
                das1 = f"$({ans_w1[0]}; {ans_w1[1]}; {ans_w1[2]})$"
                das2 = f"$({ans_w2[0]}; {ans_w2[1]}; {ans_w2[2]})$"
                das3 = f"$({ans_w3[0]}; {ans_w3[1]}; {ans_w3[2]})$"

                # Câu hỏi
                noidungcauhoi = (
                    f"Trong không gian với hệ tọa độ $Oxyz$, cho hai điểm $A({xA}; {yA}; {zA})$ và $B({xB}; {yB}; {zB})$. "
                    f"Vectơ $\\overrightarrow{{AB}}$ có tọa độ là"
                )

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = (
                    f"Ta có công thức tọa độ của vectơ $\\overrightarrow{{AB}} = (x_B - x_A; y_B - y_A; z_B - z_A)$.\\\\ \n"
                    f"Thay tọa độ các điểm $A$, $B$ vào công thức ta được:\\\\ \n"
                    f"$\\overrightarrow{{AB}} = ({xB} - {fm(xA)}; {yB} - {fm(yA)}; {zB} - {fm(zA)}) = ({ans_correct[0]}; {ans_correct[1]}; {ans_correct[2]})$.\\\\ \n"
                    f"Vậy tọa độ của vectơ $\\overrightarrow{{AB}}$ là $({ans_correct[0]}; {ans_correct[1]}; {ans_correct[2]})$."
                )

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

