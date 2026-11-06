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


def bt_dang17_p1_b2_c6_ds10(self):
            #Khai báo biến
            # Khai báo biến và chọn dạng (giữ nguyên cấu trúc mẫu)
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 3: Suy nghĩ tìm cách random bài toán
                # m11: số học sinh nam khối 11
                # m12: số học sinh nam khối 12
                # f12: số học sinh nữ khối 12
                m11 = randint(2, 3)
                m12 = randint(7, 9)
                f12 = randint(3, 4)
                tong_hs = m11 + m12 + f12

                # Tính số phần tử không gian mẫu n(Omega) = C(tong_hs, 3)
                n_omega = math.comb(tong_hs, 3)

                # Tính các trường hợp thuận lợi cho biến cố A
                # TH1: 1 học sinh khối 11, 1 nam khối 12, 1 nữ khối 12
                th1 = m11 * m12 * f12
                # TH2: 1 học sinh khối 11, 2 nữ khối 12
                th2 = m11 * math.comb(f12, 2)
                # TH3: 2 học sinh khối 11, 1 nữ khối 12
                th3 = math.comb(m11, 2) * f12

                n_a = th1 + th2 + th3

                # Rút gọn phân số xác suất
                common = math.gcd(n_a, n_omega)
                tu_so = n_a // common
                mau_so = n_omega // common

                # Đáp án đúng
                da_dung = '\\frac{%s}{%s}' % (tu_so, mau_so)

                # Bước 4: Điều chỉnh các phương án sai không được phép trùng với đáp án đúng
                s = []
                while len(s) < 3:
                    sai_tu = n_a + randint(-15, 15)
                    if sai_tu > 0 and sai_tu < n_omega:
                        gc = math.gcd(sai_tu, n_omega)
                        f_sai = '\\frac{%s}{%s}' % (sai_tu // gc, n_omega // gc)
                        if f_sai != da_dung and f_sai not in s:
                            s.append(f_sai)

                # Câu hỏi
                noidungcauhoi = ('Có %s học sinh của một trường THPT đạt danh hiệu học sinh xuất sắc trong đó khối 12 có %s học sinh nam và %s học sinh nữ, khối 11 có %s học sinh nam. Chọn ngẫu nhiên 3 học sinh bất kỳ để trao thưởng, xác suất để 3 học sinh được chọn có cả nam và nữ đồng thời có cả khối 11 và khối 12 là'
                                 % (latex(tong_hs), latex(m12), latex(f12), latex(m11)))

                # Các đáp án
                da_d = ('\\True $%s$' % da_dung)
                da_s1 = '$%s$' % s[0]
                da_s2 = '$%s$' % s[1]
                da_s3 = '$%s$' % s[2]

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (Viết chi tiết, không viết tắt)
                loigiai = ('Không gian mẫu là số cách chọn ngẫu nhiên 3 học sinh từ %s học sinh. \\\\'
                           'Suy ra số phần tử của không gian mẫu là $n\\left(\\Omega\\right) = C_{%s}^{3} = %s$. \\\\'
                           'Gọi $A$ là biến cố 3 học sinh được chọn có cả nam và nữ đồng thời có cả khối 11 và khối 12. \\\\'
                           'Ta có các trường hợp thuận lợi cho biến cố $A$ là: \\\\'
                           'Trường hợp 1: Chọn 1 học sinh khối 11, 1 học sinh nam khối 12 và 1 học sinh nữ khối 12 nên có $C_{%s}^{1}C_{%s}^{1}C_{%s}^{1} = %s$ cách. \\\\'
                           'Trường hợp 2: Chọn 1 học sinh khối 11, 2 học sinh nữ khối 12 nên có $C_{%s}^{1}C_{%s}^{2} = %s$ cách. \\\\'
                           'Trường hợp 3: Chọn 2 học sinh khối 11, 1 học sinh nữ khối 12 nên có $C_{%s}^{2}C_{%s}^{1} = %s$ cách. \\\\'
                           'Suy ra số phần tử của biến cố $A$ là $n\\left(A\\right) = %s + %s + %s = %s$. \\\\'
                           'Vậy xác suất cần tính là $P\\left(A\\right) = \\frac{n\\left(A\\right)}{n\\left(\\Omega\\right)} = \\frac{%s}{%s} = %s$.'
                           % (latex(tong_hs), latex(tong_hs), latex(n_omega),
                              latex(m11), latex(m12), latex(f12), latex(th1),
                              latex(m11), latex(f12), latex(th2),
                              latex(m11), latex(f12), latex(th3),
                              latex(th1), latex(th2), latex(th3), latex(n_a),
                              latex(n_a), latex(n_omega), da_dung))

            # Xuất câu trắc nghiệm (Phần content không dùng tiền tố r)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + 
                '\n\\choice \n'
                '{' + str(list_1[0]) + '}\n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

