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


def bt_dang30_p1_b2_c6_ds10(self):
            #Khai báo biến
            # Khai báo biến và chọn dạng (giữ nguyên cấu trúc mẫu)
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3: Suy nghĩ tìm cách random bài toán
                # m: số học sinh nam, n: số học sinh nữ
                m = random.randint(7, 9) 
                n = random.randint(3, 4)
                tong = m + n
                gaps = m + 1

                # Tính toán không gian mẫu
                n_omega_val = factorial(tong)

                # Tính số kết quả thuận lợi cho biến cố A (Xếp n nữ không cạnh nhau)
                # Bước 1: Xếp m nam có m! cách
                # Bước 2: Chọn n vị trí từ m+1 khoảng trống và xếp n nữ vào đó: A_{m+1}^n
                # Công thức: n(A) = m! * (m+1)! / (m+1-n)!
                n_A_val = factorial(m) * (factorial(gaps) // factorial(gaps - n))

                # Tính xác suất
                prob = Rational(n_A_val, n_omega_val)

                # B4: Điều chỉnh các phương án sai không trùng với đáp án đúng
                da = '$%s$' % (latex(prob))

                # Tạo các phương án nhiễu (phương án sai)
                s = set()
                while len(s) < 3:
                    # Nhiễu 1: Dùng phần bù (1 - P)
                    sai1 = 1 - prob
                    # Nhiễu 2: Sai sót do dùng tổ hợp thay vì chỉnh hợp ở bước xếp nữ
                    n_A_sai = factorial(m) * (factorial(gaps) // (factorial(n) * factorial(gaps - n)))
                    sai2 = Rational(n_A_sai, n_omega_val)
                    # Nhiễu 3: Một phân số ngẫu nhiên có cùng mẫu hoặc mẫu gần giống
                    sai3 = Rational(random.randint(1, prob.q - 1), prob.q)

                    for item in [sai1, sai2, sai3]:
                        if item != prob:
                            s.add('$%s$' % (latex(item)))

                    # Nếu vẫn thiếu, thêm ngẫu nhiên
                    if len(s) < 3:
                        s.add('$%s$' % (latex(Rational(random.randint(1, 20), random.randint(21, 100)))))

                list_sai = list(s)
                das1 = list_sai[0]
                das2 = list_sai[1]
                das3 = list_sai[2]

                # Câu hỏi (B2: Viết lại y hệt nội dung bài toán)
                noidungcauhoi = ('''Đội tuyển học sinh giỏi của một trường THPT có $%s$ học sinh nam và $%s$ học sinh nữ. Trong buổi lễ trao phần thưởng, các học sinh trên được xếp thành một hàng ngang. Xác suất để khi xếp sao cho $%s$ học sinh nữ không đứng cạnh nhau bằng'''
                                 % (latex(m), latex(n), latex(n)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (B2: Viết chi tiết giống nội dung ảnh, không viết tắt)
                # Sử dụng \\left( và \\right) theo yêu cầu
                loigiai = ('''Không gian mẫu là số cách sắp xếp tất cả $%s$ học sinh thành một hàng ngang. Suy ra số phần tử của không gian mẫu là $n\\left(\\Omega\\right) = %s!$. \\\\
                            Gọi $A$ là biến cố "Xếp các học sinh trên thành một hàng ngang mà $%s$ học sinh nữ không đứng cạnh nhau". Ta mô tả khả năng thuận lợi của biến cố $A$ như sau: \\\\
                            + Đầu tiên xếp $%s$ học sinh nam thành một hàng ngang, có $%s!$ cách. \\\\
                            + Sau đó xem $%s$ học sinh này như $%s$ vách ngăn nên có $%s$ vị trí để xếp $%s$ học sinh nữ thỏa mãn yêu cầu bài toán (gồm $%s$ vị trí giữa $%s$ học sinh và $2$ vị trí hai đầu). Do đó có $A_{%s}^{%s}$ cách xếp $%s$ học sinh nữ. \\\\
                            Suy ra số phần tử của biến cố $A$ là $n\\left(A\\right) = %s! \\cdot A_{%s}^{%s}$. \\\\
                            Vậy xác suất cần tính $P\\left(A\\right) = \\frac{%s! \\cdot A_{%s}^{%s}}{%s!} = %s$.'''
                           % (latex(tong), latex(tong), latex(n),
                              latex(m), latex(m),
                              latex(m), latex(m), latex(gaps), latex(n),
                              latex(m - 1), latex(m), latex(gaps), latex(n), latex(n),
                              latex(m), latex(gaps), latex(n),
                              latex(m), latex(gaps), latex(n), latex(tong), latex(prob)))

            # Xuất câu trắc nghiệm (Không dùng tiền tố r, đảm bảo format content)
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 

