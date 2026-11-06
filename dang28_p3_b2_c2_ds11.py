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


def bt_dang28_p3_b2_c2_ds11(self):
            # Khai báo biến
            # --- KHỞI TẠO THAM SỐ RANDOM ---
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # 1. RANDOM CÁC THAM SỐ ĐẦU VÀO
                # Lương khởi điểm u1 (USD): Chọn số tròn nghìn
                u1 = random.randrange(30000, 55000, 1000) 

                # Mức tăng d (USD): Chọn số tròn trăm
                d = random.randrange(1200, 3200, 200)

                # Số năm làm việc n (ĐÁP ÁN): Số nguyên nhỏ hợp lý
                n = random.randint(6, 15)

                # 2. TÍNH TỔNG LƯƠNG Sn (Giá trị cần tìm trong đề bài)
                # Sn = n/2 * [2*u1 + (n-1)*d]
                Sn = Rational(n, 2) * (2 * u1 + (n - 1) * d)

                # 3. CHUẨN BỊ ĐÁP ÁN
                kq = latex(n) # Đáp án đúng n

                # Tạo đáp án đúng và các đáp án sai
                du = ['$%s$'%(kq),
                      ]
                da = random.choice(du)

                # Tạo các đáp án sai (số nguyên gần n)
                s = ['$%s$'%(latex(n+1)),
                     '$%s$'%(latex(n+2)),
                     '$%s$'%(latex(n-1)),
                     '$%s$'%(latex(n-2)),
                     '$%s$'%(latex(n+3)),
                     '$%s$'%(latex(n-3)),
                    ]

                # Chọn ngẫu nhiên 3 đáp án sai khác nhau
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # 4. TẠO NỘI DUNG CÂU HỎI
                noidungcauhoi = ('''Nếu anh Nam nhận được lời mời việc cho một công ty nước ngoài với mức lương khởi điểm là $%s$ đô la mỗi năm và được tăng thêm $%s$ đô la mỗi năm, thì sẽ mất bao nhiêu năm làm việc để tổng lương mà anh Nam nhận được là $%s$ đô la?'''
                                 %(latex(u1), latex(d), latex(Sn)
                                 ))

                # 5. ĐỊNH DẠNG ĐÁP ÁN TRẮC NGHIỆM
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách và trộn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # 6. TẠO NỘI DUNG LỜI GIẢI
                loigiai=('''Bài toán tính số năm làm việc để đạt tổng lương nhất định là bài toán cấp số cộng, trong đó:
                          \\begin{itemize}
                              \\item Lương khởi điểm: $u_1 = %s$
                              \\item Mức tăng hàng năm (công sai): $d = %s$
                              \\item Tổng lương: $S_n = %s$
                          \\end{itemize}
                          Áp dụng công thức tính tổng $n$ số hạng đầu của cấp số cộng:
                          $$S_n = \\frac{n}{2}\\left[2u_1+(n-1)d\\right]$$
                          Thay các giá trị đã biết vào công thức, ta có phương trình:
                          $$%s = \\frac{n}{2}\\left[2\\cdot %s+(n-1)\\cdot %s\\right]$$
                          Giải phương trình trên, ta tìm được $n = %s$. \\\\
                          Vậy anh Nam cần làm việc %s năm để tổng lương nhận được là $%s$ đô la.'''
                          %(latex(u1), latex(d), latex(Sn),
                            latex(Sn), latex(u1), latex(d),
                            latex(n), latex(n), latex(Sn)
                          ))
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(n))


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

