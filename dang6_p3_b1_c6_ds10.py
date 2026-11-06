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


def bt_dang6_p3_b1_c6_ds10(self):
            # Khai báo biến
            # Random số lượng mỗi bên (n nam, n nữ) để đảm bảo có 2 trường hợp xen kẽ
            n = random.randint(2, 3) 
            tong_so_nguoi = 2 * n

            list_ten_nam = ["Mạnh", "Dũng", "Tuấn", "Hùng", "Minh", "Hoàng", "Nam", "Việt", "Kiên", "Lâm"]
            list_ten_nu = ["Hoa", "Lan", "Mai", "Linh", "Chi", "Hương", "Quỳnh", "Trang", "Ngọc", "An"]

            # Chọn ngẫu nhiên n nam và n nữ
            nam_chon = random.sample(list_ten_nam, n)
            nu_chon = random.sample(list_ten_nu, n)

            # Tạo danh sách tên và kí hiệu thứ tự (Ví dụ: n=2 là MDHL, n=3 là MDTHLM)
            tat_ca_ten = nam_chon + nu_chon
            ky_hieu = "".join([t[0] for t in tat_ca_ten])
            chuoi_ten_thu_tu = ", ".join(tat_ca_ten)

            # B4: Tính toán đáp án đúng và tạo các phương án sai
            # Công thức: 2 * (n! * n!)
            n_giai_thua = math.factorial(n)
            so_cach_1_case = n_giai_thua * n_giai_thua
            kq_dung = 2 * so_cach_1_case

            # Tạo các phương án sai
            s = set()
            s.add(str(math.factorial(tong_so_nguoi))) # Hoán vị tất cả
            s.add(str(so_cach_1_case))                # Chỉ tính 1 trường hợp
            s.add(str(kq_dung + n*2))
            s.add(str(kq_dung * 2))
            s.add(str(n_giai_thua + n_giai_thua))
            s.add(str(kq_dung // 2) if kq_dung > 4 else "10")
            s.add(str(kq_dung + 10))

            # Loại bỏ giá trị trùng với đáp án đúng và chuyển thành list
            s = [x for x in s if x != str(kq_dung)]
            random.shuffle(s)

            das1 = s[0]
            das2 = s[1]
            das3 = s[2]

            # B2: Viết lại nội dung câu hỏi và lời giải chi tiết
            noidungcauhoi = ('''Một nhóm bạn có $%s$ bạn gồm $%s$ bạn nam là %s và $%s$ nữ là %s được xếp ngẫu nhiên trên một ghế dài. Kí hiệu $%s$ là cách sắp xếp theo thứ tự: %s. Số phần tử của biến cố $B$: "xếp nam và nữ ngồi xen kẽ nhau" bằng bao nhiêu?'''
                            %(latex(tong_so_nguoi), latex(n), ", ".join(nam_chon), latex(n), ", ".join(nu_chon), ky_hieu, chuoi_ten_thu_tu))

            # Xác định vị trí ghế dựa trên n
            ghe_nam_t1 = ", ".join([str(i) for i in range(1, tong_so_nguoi + 1) if i % 2 != 0])
            ghe_nu_t1 = ", ".join([str(i) for i in range(1, tong_so_nguoi + 1) if i % 2 == 0])

            loigiai = ('''Trường hợp 1: bạn nam ngồi đầu. \\\\
            Khi đó $%s$ bạn nam xếp vào $%s$ chỗ (số ghế $%s$) có $%s!$ cách, nữ xếp vào $%s$ chỗ còn lại (ghế số $%s$) có $%s!$ cách. \\\\
            Suy ra: số cách xếp là $%s! \\cdot %s! = %s$ cách. \\\\
            Trường hợp 2: bạn nữ ngồi đầu. Tương tự có %s cách xếp. \\\\
            Vậy theo quy tắc cộng số phần tử của biến cố $B$ là $%s + %s = %s$.'''
                      %(latex(n), latex(n), ghe_nam_t1, latex(n), latex(n), ghe_nu_t1, latex(n), 
                        latex(n), latex(n), latex(so_cach_1_case), latex(so_cach_1_case), 
                        latex(so_cach_1_case), latex(so_cach_1_case), latex(kq_dung)))
            dapan=' \\shortans[0]{$%s$} '%(latex(kq_dung))
            # Các đáp án
            da_d = ('\\True ' + str(kq_dung))
            da_s1 = str(das1)
            da_s2 = str(das2)
            da_s3 = str(das3)

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content  

