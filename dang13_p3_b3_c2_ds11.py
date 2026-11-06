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


def bt_dang13_p3_b3_c2_ds11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # 1. Random hóa dữ liệu đề bài
                a_canh = random.choice([12, 16, 20, 24, 28]) 
                n_lan = random.randint(4, 6)   

                # 2. TÍNH TOÁN
                u1 = Rational(a_canh**2, 4) 
                q = Rational(1, 2)

                # Tính toán chính xác
                tong_dien_tich_exact = u1 * (1 - q**n_lan) / (1 - q)

                # Các thành phần cần thiết cho Lời giải
                hai_mu_n = 2**n_lan
                tu_so_phan_so = hai_mu_n - 1

                # Làm tròn kết quả cuối cùng đến 1 chữ số thập phân
                kq2 = float(tong_dien_tich_exact)
                kq3 = Decimal(kq2).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
                kq=str(kq3).replace('.',',')

                # 3. ĐÁP ÁN TRẮC NGHIỆM

                da = f'${kq}$'

                s = [f'$%s$'%(latex(round(kq2 + 0.1, 1))).replace('.',','),
                     f'$%s$'%(latex(round(kq2 + 0.2, 1))).replace('.',','),
                     f'$%s$'%(latex(round(kq2 - 0.1, 1))).replace('.',','),
                     f'$%s$'%(latex(round(kq2 - 0.2, 1))).replace('.',','),
                     f'$%s$'%(latex(round(kq2 + 0.5, 1))).replace('.',','),
                     f'$%s$'%(latex(round(kq2 - 0.5, 1))).replace('.',','),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # 4. CÂU HỎI
                noidungcauhoi = ('''Các cạnh của hình vuông ban đầu có chiều dài $%s$ cm. Một hình vuông mới được hình thành bằng cách nối các điểm giữa của các cạnh của hình vuông ban đầu và một trong số các hình tam giác kết quả được tô màu. Nếu quá trình này được lặp lại $%s$ lần nữa, tổng diện tích vùng được tô màu bằng bao nhiêu? (làm tròn kết quả đến hàng đơn vị).'''
                                  %(latex(a_canh),latex(n_lan)
                                  ))

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # 5. NỘI DUNG LỜI GIẢI
                # TỔNG CỘNG CÓ 14 LẦN DÙNG %s - ĐÃ KIỂM TRA LẠI CHUỖI VÀ ĐỐI SỐ
                loigiai=('''Gọi $a$ là độ dài cạnh của hình vuông ban đầu. Theo đề bài $a = %s$ cm. \\\\
                            Gọi $u_n$ là diện tích hai tam giác được tô màu ở lần thực hiện thứ $n$. \\\\
                            Ở lần 1: Diện tích 2 tam giác tô màu là: $u_1 = \\frac{a^2}{4}$. \\\\
                            Thay số: $u_1 = \\frac{%s^2}{4} = %s$ (cm$^2$). \\\\
                            Dãy diện tích $(u_n)$ là cấp số nhân với số hạng đầu $u_1 = %s$ và công bội $q = \\frac{1}{2}$. \\\\
                            Tổng diện tích sau $n = %s$ lần lặp lại là $S_{%s}$: \\\\
                            $S_{%s} = u_1 \\cdot \\frac{1-q^{%s}}{1-q} = %s \\cdot \\frac{1 - (\\frac{1}{2})^{%s}}{1 - \\frac{1}{2}}$ \\\\
                            $S_{%s} = %s \\cdot 2 \\cdot \\left(1 - \\frac{1}{%s}\\right) = %s \\cdot \\frac{%s}{%s} \\approx %s \\text{ (cm}^2\\text{)}$.''' 

                          # PHẦN ĐỐI SỐ: CÓ 14 ĐỐI SỐ TƯƠNG ỨNG VỚI 14 LẦN %s
                          %(latex(a_canh),                  # 1
                            latex(a_canh),latex(u1),         # 2, 3
                            latex(u1),                       # 4
                            latex(n_lan),latex(n_lan),       # 5, 6
                            latex(n_lan),latex(n_lan),       # 7, 8
                            latex(u1),                       # 9
                            latex(n_lan),                    # 10
                            latex(n_lan),                    # 11
                            latex(u1),                       # 12
                            latex(hai_mu_n),                 # 13 (2^n)
                            latex(u1*2),                     # 14 (2 * u1)
                            latex(tu_so_phan_so),            # 15 (2^n - 1)
                            latex(hai_mu_n),                 # 16 (2^n)
                            kq                               # 17 (Cần 17 đối số. Tôi đã đếm lại. Chuỗi dài hơn tôi nghĩ.)
                          ))
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))  

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')               
            return content 

