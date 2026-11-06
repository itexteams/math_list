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


def bt_dang12_p3_b1_c6_ds10(self):
            # Khai báo biến
            # Khai báo biến và chọn dạng (ở đây chỉ có 1 dạng theo yêu cầu)
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3-Suy nghĩ tìm cách random bài toán
                # Số đội tham gia phải là số chẵn để chia làm 2 bảng bằng nhau
                # Chọn số đội tổng cộng (N) từ 10, 12, 14, 16
                N = random.choice([10, 12, 14, 16])
                K = N // 2 # Số đội mỗi bảng

                # Random tên lớp
                ds_lop = ['10\\text{A}1', '10\\text{A}2', '10\\text{A}5', '11\\text{B}1', '11\\text{B}2', '12\\text{C}1', '12\\text{C}3', '10\\text{A}3', '11\\text{A}2']
                random.shuffle(ds_lop)
                lop1 = ds_lop[0]
                lop2 = ds_lop[1]

                # Tính toán số phần tử của biến cố
                # Bước 1: Chọn 1 trong 2 bảng (A hoặc B) để đặt 2 đội cụ thể vào: 2 cách
                # Bước 2: Chọn K-2 đội từ N-2 đội còn lại để lấp đầy bảng đó: C(N-2, K-2) cách
                # Bước 3: K đội còn lại tự động vào bảng còn lại: 1 cách
                to_hop = math.comb(N - 2, K - 2)
                ket_qua = 2 * to_hop

                # Đáp án đúng
                da = '$%s$' % (latex(ket_qua))

                # B4-Điều chỉnh các phương án sai không được phép trùng với đáp án đúng
                s = []
                # Phương án sai 1: Quên nhân 2 (chỉ tính cho 1 bảng cố định)
                s.append('$%s$' % (latex(to_hop)))
                # Phương án sai 2: Tính tổng số cách chia bảng rồi chia đôi (không liên quan điều kiện)
                s.append('$%s$' % (latex(math.comb(N, K))))
                # Phương án sai 3: Một số ngẫu nhiên lân cận
                s.append('$%s$' % (latex(ket_qua + random.choice([10, 20, -10]))))
                # Phương án sai 4: C(N-2, K-1)
                s.append('$%s$' % (latex(math.comb(N - 2, K - 1))))

                # Lọc bỏ các giá trị trùng với đáp án đúng và lấy 3 phương án sai
                s = [x for x in s if x != da]
                s = list(set(s)) # Xóa trùng trong list s
                while len(s) < 3:
                    random_val = ket_qua + random.randint(5, 50)
                    if '$%s$' % (latex(random_val)) != da:
                        s.append('$%s$' % (latex(random_val)))

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # B2-Viết lại y hệt bài toán gồm đề bài và lời giải
                # Câu hỏi
                noidungcauhoi = ('''Trong giải bóng đá nữ ở trường THPT có $%s$ đội tham gia, trong đó có hai đội của hai lớp $%s$ và $%s$. Ban tổ chức tiến hành bốc thăm ngẫu nhiên để chia thành hai bảng đấu $A, B$ mỗi bảng $%s$ đội. Số phần tử của biến cố để 2 đội của hai lớp $%s$ và $%s$ ở cùng một bảng bằng bao nhiêu?'''
                                 % (latex(N), lop1, lop2, latex(K), lop1, lop2))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết (Bản dịch từ ảnh và thay số)
                loigiai = ('''Gọi $A$ là biến cố: "2 đội của hai lớp $%s$ và $%s$ ở cùng một bảng". \\\\
                             Để hai đội này ở cùng một bảng, ta có hai trường hợp: \\\\
                             Trường hợp 1: Hai đội cùng nằm ở bảng $A$. Khi đó, ta cần chọn thêm $%s - 2 = %s$ đội từ $%s - 2 = %s$ đội còn lại để vào bảng $A$. Số cách chọn là $C_{%s}^{%s} = %s$ cách. \\\\
                             Trường hợp 2: Hai đội cùng nằm ở bảng $B$. Tương tự, ta chọn thêm $%s$ đội từ $%s$ đội còn lại vào bảng $B$. Số cách chọn là $C_{%s}^{%s} = %s$ cách. \\\\
                             Vì hai bảng $A$ và $B$ là phân biệt, nên tổng số phần tử của biến cố $A$ là: \\\\
                             $n\\left( A \\right) = C_{%s}^{%s} + C_{%s}^{%s} = C_{%s}^{%s} \\cdot 2! = %s$.'''
                           % (lop1, lop2, 
                              latex(K), latex(K-2), latex(N), latex(N-2), latex(N-2), latex(K-2), latex(to_hop),
                              latex(K-2), latex(N-2), latex(N-2), latex(K-2), latex(to_hop),
                              latex(N-2), latex(K-2), latex(N-2), latex(K-2), latex(N-2), latex(K-2), latex(ket_qua)))
                dapan=' \\shortans[0]{$%s$} '%(latex(ket_qua))
            # Xuất câu trắc nghiệm theo đúng cấu trúc mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content  

