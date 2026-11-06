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


def bt_dang33_p1_b2_c6_ds10(self):
            #Khai báo biến
            # Khai báo biến và chọn dạng (giữ nguyên cấu trúc mẫu)
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # B3: Random số lượng học sinh nam (m) và nữ (n)
                # Để đảm bảo bài toán có nghiệm (không có 2 nữ cạnh nhau), số nam m >= số nữ n
                m = randint(5, 7)  # Số học sinh nam
                n = randint(3, m-1)  # Số học sinh nữ (ít hơn nam để dễ xếp)
                tong_hs = m + n

                # Tính toán không gian mẫu
                # Xếp (m+n) người vào bàn tròn: (m+n-1)!
                n_omega_val = factorial(tong_hs - 1)
                n_omega_tex = str(tong_hs - 1) + '!'

                # Tính số cách xếp thỏa mãn (biến cố A)
                # 1. Cố định 1 nam, xếp m-1 nam còn lại: (m-1)! cách
                xep_nam = factorial(m - 1)
                # 2. Xếp n nữ vào m khoảng trống giữa m nam: A_m^n cách
                # Công thức: A_m^n = m! / (m-n)!
                chinh_hop_nu = Rational(factorial(m), factorial(m - n))
                n_A = xep_nam * chinh_hop_nu

                # Tính xác suất
                prob = Rational(n_A, n_omega_val)

                # Đáp án đúng
                da = '$%s$' % (latex(prob))

                # B4: Tạo các phương án sai (không trùng đáp án đúng)
                s = []
                # Phương án sai 1: Nhầm sang hoán vị hàng ngang (n! / (m+n)!)
                sai1 = Rational(factorial(m) * factorial(n), factorial(tong_hs))
                # Phương án sai 2: Nhầm công thức chỉnh hợp thành tổ hợp
                sai2 = Rational(xep_nam * binomial(m, n), n_omega_val)
                # Phương án sai 3: Đảo ngược phân số hoặc thay đổi tử số
                sai3 = Rational(prob.p + 1, prob.q)
                # Phương án sai 4: Thay đổi mẫu số
                sai4 = Rational(prob.p, prob.q + 2)

                list_sai = [sai1, sai2, sai3, sai4]
                for phuongan in list_sai:
                    tex_sai = '$%s$' % (latex(phuongan))
                    if tex_sai != da:
                        s.append(tex_sai)

                # Lấy 3 đáp án sai ngẫu nhiên
                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Xếp $%s$ học sinh nam và $%s$ học sinh nữ vào một bàn tròn $%s$ ghế. Xác suất để không có học sinh nữ nào ngồi cạnh nhau bằng'''
                                 %(latex(m), latex(n), latex(tong_hs)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (Viết chi tiết, không viết tắt, dùng \left( \right))
                loigiai = ('''Cố định 1 vị trí cho 1 học sinh nam hoặc nữ, đánh dấu các ghế còn lại từ 1 đến $%s$. \\\\
                           Không gian mẫu là số hoán vị của $%s$ học sinh $\\left( \\text{còn lại không cố định} \\right)$ trên $%s$ ghế đánh dấu. \\\\
                           Suy ra số phần tử của không gian mẫu là $n\\left( \\Omega \\right) = %s!$. \\\\
                           Gọi $A$ là biến cố "không có hai học sinh nữ nào ngồi cạnh nhau". Ta mô tả khả năng thuận lợi của biến cố $A$ như sau: \\\\
                           - Đầu tiên ta cố định một học sinh nam, $%s$ học sinh nam còn lại có $%s!$ cách xếp. \\\\
                           - Ta xem $%s$ học sinh nam như $%s$ vách ngăn trên vòng tròn, thế thì sẽ tạo ra $%s$ ô trống để ta xếp $%s$ học sinh nữ vào $\\left( \\text{mỗi ô trống chỉ xếp được xếp 1 học sinh nữ} \\right)$. Do đó có $A_{%s}^{%s}$ cách. \\\\
                           Suy ra $n\\left( A \\right) = %s! \\cdot A_{%s}^{%s}$. \\\\
                           Vậy xác suất cần tìm là $P\\left( A \\right) = \\frac{%s! \\cdot A_{%s}^{%s}}{%s!} = %s$.'''
                           %(latex(tong_hs - 1), latex(tong_hs - 1), latex(tong_hs - 1), latex(tong_hs - 1),
                             latex(m - 1), latex(m - 1), latex(m), latex(m), latex(m), latex(n),
                             latex(m), latex(n), latex(m - 1), latex(m), latex(n),
                             latex(m - 1), latex(m), latex(n), latex(tong_hs - 1), latex(prob)
                            ))

            # Xuất câu trắc nghiệm (Không dùng tiền tố r)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

