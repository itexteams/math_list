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


def bt_dang68_p3_b2_c6_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random số lượng lá thư từ 6 đến 9 (để đảm bảo có thể chia đúng 3 lá vào 1 hòm)
                n_thu = randint(6, 9)
                k_target = 3  # Số lá thư trong hòm đích cố định là 3 như đề bài

                # Tính số phần tử không gian mẫu: n(Omega) = 3^n_thu
                n_omega = 3**n_thu

                # Bước 1: Chọn hòm chứa đúng 3 lá: C_3^1 = 3
                chon_hom = 3

                # Bước 2: Chọn 3 lá thư trong n_thu lá thư cho hòm đó: C_n^3
                chon_thu = binomial(n_thu, k_target)

                # Bước 3: Phân phối số thư còn lại (n_thu - 3) vào 2 hòm còn lại
                con_lai = n_thu - k_target

                # Tổng số cách phân phối ngẫu nhiên thư còn lại vào 2 hòm: 2^(con_lai)
                tong_cach_2_hom = 2**con_lai

                # Loại trừ trường hợp hòm còn lại chứa đúng 3 lá thư: 2 * C_(con_lai)^3
                tru_truong_hop = 2 * binomial(con_lai, k_target)

                # Số cách phân phối hợp lệ cho 2 hòm còn lại
                cach_2_hom_hop_le = tong_cach_2_hom - tru_truong_hop

                # Tính n(A)
                n_A = chon_hom * chon_thu * cach_2_hom_hop_le

                # Tính xác suất dưới dạng số thực
                xs_value = float(n_A) / float(n_omega)

                # Làm tròn đến hàng phần trăm sử dụng Decimal
                kq3 = Decimal(str(xs_value)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                kq = str(kq3).replace('.', ',')

                # Các đáp án trắc nghiệm
                da = '$%s$' % (kq)

                # Tạo các phương án nhiễu bằng cách tăng/giảm giá trị đáp án đúng
                s = []
                for sai_val in [0.05, 0.12, 0.18, -0.05, -0.12, -0.18]:
                    val = float(kq3) + sai_val
                    if 0 < val < 1:
                        val_dec = Decimal(str(val)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                        s.append('$%s$' % str(val_dec).replace('.', ','))

                s = list(set(s))  # Loại bỏ trùng lặp nếu có
                if da in s:
                    s.remove(da)

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Có $%s$ lá thư khác nhau được bỏ ngẫu nhiên vào $3$ hòm thư khác nhau A, B, C. Xác suất để có đúng một hòm thư chứa $3$ lá thư bằng bao nhiêu? (Kết quả làm tròn đến hàng phần trăm).'''
                                 % (latex(n_thu)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Tạo danh sách các bộ số thỏa mãn điều kiện cho lời giải trực quan
                cac_bo = []
                for i in range(con_lai + 1):
                    j = con_lai - i
                    if i != 3 and j != 3:
                        cac_bo.append('(%s,%s)' % (i, j))
                str_cac_bo = ','.join(cac_bo)

                # Nội dung lời giải
                loigiai = ('''Mỗi lá thư có $3$ cách chọn hòm nên số phần tử của không gian mẫu là $n(\\Omega) = 3^{%s} = %s$.\\\\
                           Gọi $A$ là biến cố ``Đúng một hòm thư chứa $3$ lá thư''.\\\\
                           Chọn hòm chứa đúng $3$ lá: $C_3^1 = 3$ và chọn $3$ lá trong $%s$ lá: $C_{%s}^3 = %s$.\\\\
                           Bỏ $%s$ lá còn lại vào $2$ hòm sao cho không hòm nào có đúng $3$ lá.\\\\
                           Các trường hợp thỏa mãn điều kiện là $%s$.\\\\
                           Tổng số cách phân $%s$ lá vào $2$ hòm: $2^{%s}$ và trường hợp có hòm chứa đúng $3$ lá thư là: $2 \\cdot C_{%s}^3 = %s$.\\\\
                           Số cách phân hợp lệ: $2^{%s} - %s = %s \\Rightarrow n(A) = 3 \\cdot %s \\cdot %s = %s$.\\\\
                           Vậy xác suất cần tìm là: $P = \\frac{n(A)}{n(\\Omega)} = \\frac{%s}{%s} \\approx %s$.'''
                           % (latex(n_thu), latex(n_omega),
                              latex(n_thu), latex(n_thu), latex(chon_thu),
                              latex(con_lai),
                              str_cac_bo,
                              latex(con_lai), latex(con_lai), latex(con_lai), latex(tru_truong_hop),
                              latex(con_lai), latex(tru_truong_hop), latex(cach_2_hom_hop_le), latex(chon_thu), latex(cach_2_hom_hop_le), latex(n_A),
                              latex(n_A), latex(n_omega), str(kq)))
                dapan='\\shortans[0]{$%s$}\n'%(str(kq))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

