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


def bt_dang32_p3_b2_c6_ds10(self):
            #Khai báo biến
            # Khai báo biến và chọn dạng (giữ nguyên cấu trúc mẫu)
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random số quyển sách mỗi môn (k), thường là 2 hoặc 3 để khớp với logic bài toán
                # Trong ảnh k = 3.
                k = random.randint(2, 3) 
                mon = ["Toán", "Lý", "Hóa", "Sinh"]
                tong_so_sach = 4 * k

                # Tính toán theo logic vách ngăn trong ảnh
                # Bước 1: Xếp k cuốn Toán làm vách ngăn -> có k+1 vị trí trống
                c1 = binomial(k + 1, k)

                # Bước 2: Xếp k cuốn Lý vào (k+1) vị trí -> tổng cộng có 2k cuốn -> 2k+1 vị trí trống
                c2 = binomial(2*k + 1, k)

                # Bước 3: Xếp k cuốn Hóa vào (2k+1) vị trí -> tổng cộng có 3k cuốn -> 3k+1 vị trí trống
                c3 = binomial(3*k + 1, k)

                # Kết quả đúng
                kq_int = c1 * c2 * c3
                da = '$%s$' % (latex(kq_int))

                # Tạo các phương án sai (đảm bảo không trùng với đáp án đúng)
                s = set()
                while len(s) < 3:
                    # Tạo sai số dựa trên việc tính nhầm tổ hợp hoặc nhân thiếu bước
                    sai1 = binomial(k + 2, k) * binomial(2*k + 1, k) * binomial(3*k + 1, k)
                    sai2 = binomial(k + 1, k) * binomial(2*k, k) * binomial(3*k, k)
                    sai3 = kq_int // 10 if kq_int > 100 else kq_int + 50
                    sai4 = kq_int + random.randint(100, 500)

                    candidates = [sai1, sai2, sai3, sai4]
                    val = random.choice(candidates)
                    if val != kq_int:
                        s.add('$%s$' % (latex(val)))

                das = list(s)
                das1 = das[0]
                das2 = das[1]
                das3 = das[2]

                # Câu hỏi
                noidungcauhoi = ('''Trong thư viện có $%s$ quyển sách bao gồm $%s$ quyển Toán giống nhau, $%s$ quyển Lý giống nhau, $%s$ quyển Hóa giống nhau và $%s$ quyển Sinh giống nhau. Số cách xếp thành một dãy sao cho $%s$ quyển sách thuộc cùng 1 môn không được xếp liền nhau bằng bao nhiêu?'''
                                 %(latex(tong_so_sach), latex(k), latex(k), latex(k), latex(k), latex(k)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)


                # Nội dung lời giải chi tiết theo yêu cầu
                loigiai = ('''Xếp ngẫu nhiên $%s$ cuốn sách Toán kề nhau. Xem $%s$ cuốn Toán là $%s$ vách ngăn, giữa $%s$ cuốn sách Toán có $%s$ vị trí trống và thêm hai vị trí đầu, tổng cộng có $%s$ vị trí trống. \\\\
                           Bước 1. Chọn $%s$ vị trí trống trong $%s$ vị trí để xếp $%s$ cuốn Lý có $C_{%s}^{%s}$ cách. \\\\
                           Bước 2. Giữa $%s$ cuốn Lý và Toán có $%s$ vị trí trống và thêm 2 vị trí đầu có tổng cộng $%s$ vị trí trống. Chọn $%s$ chỗ trống trong $%s$ vị trí trống để xếp $%s$ cuốn Hóa có $C_{%s}^{%s}$ cách. \\\\
                           Bước 3. Giữa $%s$ cuốn sách Toán, Lý, Hóa đã xếp có $%s$ vị trí trống và thêm 2 vị trí đầu, tổng có $%s$ vị trí trống. Chọn $%s$ vị trí trong $%s$ vị trí trống để xếp $%s$ cuốn Sinh có $C_{%s}^{%s}$ cách. \\\\
                           Vậy theo quy tắc nhân có $C_{%s}^{%s} \\cdot C_{%s}^{%s} \\cdot C_{%s}^{%s} = %s$ cách.'''
                           %(latex(k), latex(k), latex(k), latex(k), latex(k-1), latex(k+1),
                             latex(k), latex(k+1), latex(k), latex(k+1), latex(k),
                             latex(2*k), latex(2*k-1), latex(2*k+1), latex(k), latex(2*k+1), latex(k), latex(2*k+1), latex(k),
                             latex(3*k), latex(3*k-1), latex(3*k+1), latex(k), latex(3*k+1), latex(k), latex(3*k+1), latex(k),
                             latex(k+1), latex(k), latex(2*k+1), latex(k), latex(3*k+1), latex(k), latex(kq_int)
                           ))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq_int))

            # Xuất nội dung theo định dạng yêu cầu (không dùng tiền tố r, dùng \left( \right))
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

