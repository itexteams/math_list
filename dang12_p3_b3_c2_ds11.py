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


def bt_dang12_p3_b3_c2_ds11(self):
            # Khai báo biến
            lisdang=['2']
            dang=random.choice(lisdang)

            if dang=='2':
                # Random các biến đầu vào cho bài toán Vi khuẩn
                # Số lượng vi khuẩn ban đầu (A)
                A = random.choice([10, 20, 15, 5, 25]) 
                # Thời gian phân đôi (T_split) - đơn vị phút
                T_split = random.choice([15, 20, 30])

                # Thời gian tổng cộng (T_total) - đơn vị giờ. Phải đảm bảo Số lần phân đôi là số nguyên
                T_total_options = {15: [1.0, 1.5, 2.0, 3.0], 20: [1.0, 2.0, 3.0], 30: [1.0, 1.5, 2.0, 2.5]}
                T_total = random.choice(T_total_options[T_split])

                # Tính toán
                # Số phút tổng cộng
                T_total_min = int(T_total * 60)
                # Số lần phân đôi (n_lan)
                n_lan = int(T_total_min / T_split)

                # Tổng số vi khuẩn sau n_lan lần phân đôi (KQ): A * 2^(n_lan)
                KQ = A * (2**n_lan)
                kq_latex = latex(KQ)

                # Tạo các đáp án trắc nghiệm
                du = ['$%s$'%(kq_latex), ]
                da = random.choice(du)

                # Đáp án sai (Chủ yếu sai lệch số mũ hoặc tính toán)
                # Cần đảm bảo các biến random thập phân được chuyển dấu
                s = ['$%s$'%(latex(KQ + 2**random.randint(1, 3))),
                     '$%s$'%(latex(A * (2**(n_lan + 1)))), # Sai lệch 1 lần phân đôi
                     '$%s$'%(latex(A * (n_lan))), # Sai công thức (nhân thay vì luỹ thừa)
                     '$%s$'%(latex(A * (n_lan * 2))), # Sai công thức (nhân với số lần nhân 2)
                     '$%s$'%(latex(int(KQ / 2))),
                     '$%s$'%(latex(int(KQ * 2))),
                     ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Chuyển dấu thập phân cho T_total nếu là số thập phân
                T_total_latex = latex(T_total).replace('.', ',')

                # Câu hỏi
                noidungcauhoi = ('''Một loại vi khuẩn được nuôi cấy trong ống nghiệm, cứ $%s$ phút lại phân đôi một lần. Nếu ban đầu có $%s$ vi khuẩn, Số lượng vi khuẩn có trong ống nghiệm sau $%s$ giờ là bao nhiêu? '''
                                  %(latex(T_split), latex(A), T_total_latex
                                  ))

                # Các đáp án
                # Cần chuyển dấu thập phân trong đáp án (nếu có)
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Áp dụng .replace('.', ',') cho các đáp án nếu chúng có chứa số thập phân
                # Trong trường hợp này, kết quả KQ là số nguyên nên không cần, 
                # nhưng nếu KQ có thể là thập phân thì cần thêm .replace

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai =('''Ta có: $%s \\text{ giờ} = %s \\text{ phút}$. \\\\
                             Số lần phân đôi trong $%s$ giờ là: $\\frac{%s}{%s}=%s$ lần. \\\\
                             Đây là bài toán cấp số nhân với số hạng đầu $u_1 = %s$ và tỉ số $q = 2$. \\\\
                             Số lượng vi khuẩn sau $n=%s$ lần phân đôi là: \\\\
                             $$u_{n+1} = u_1 \\cdot q^{n} = %s \\cdot 2^{%s} = %s$$ \\\\
                             Vậy sau $%s$ giờ, trong ống nghiệm có $%s$ vi khuẩn.'''
                          %(T_total_latex, latex(T_total_min),
                            T_total_latex, latex(T_total_min), latex(T_split), latex(n_lan),
                            latex(A),
                            latex(n_lan), latex(A), latex(n_lan), latex(KQ),
                            T_total_latex, latex(KQ)
                          ))
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(KQ))                 

            # --- XUẤT CÂU TRẮC NGHIỆM ---
            # Áp dụng .replace('.', ',') cho toàn bộ nội dung cuối cùng
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('.', ',').replace(',0', '') 
            return content 

