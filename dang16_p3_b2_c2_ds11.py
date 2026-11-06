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


def bt_dang16_p3_b2_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # --- Random hóa Dữ liệu (B3) ---
                u1 = 2 * randint(5, 20)  # Số hạng đầu (quãng đường giây 1)
                d = 4 * randint(5, 10)   # Công sai (sự khác biệt giữa các quãng đường), chọn là bội của 4
                n = randint(5, 12)       # Số giây cần tính tổng

                # --- Tính toán kết quả ---
                # Công thức tổng n số hạng đầu: S_n = n * (2*u1 + (n-1)*d) / 2
                Sn = n * (2*u1 + (n-1)*d) / 2

                # Tính các số hạng đầu để đưa vào đề bài
                u2 = u1 + d
                u3 = u2 + d
                u4 = u3 + d

                kq = Sn
                kq_str = str(int(kq)) # Kết quả là số nguyên

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(kq_str)]
                da= random.choice(du)

                # Tạo các đáp án sai
                # Lượng chênh lệch ngẫu nhiên
                delta1 = randint(1, 4) * d // 2 
                delta2 = randint(1, 5) * 10

                da_sai_list = [
                    int(kq) + delta1,
                    int(kq) - delta1,
                    int(kq) + delta2,
                    int(kq) - delta2,
                ]
                # Thêm một số đáp án sai có liên quan đến công thức
                if n > 1:
                    da_sai_list.append(int(kq) + u1) # Sai do cộng thêm u1
                    da_sai_list.append(int(kq) - d)  # Sai do trừ đi d

                da_sai_list = list(set(da_sai_list)) # Loại bỏ trùng lặp
                if int(kq) in da_sai_list:
                    da_sai_list.remove(int(kq))

                # Định dạng các đáp án sai dưới dạng LaTeX
                s = []
                for val in da_sai_list:
                    s.append('$%s$'%(str(val)))

                if len(s) < 3: # Đảm bảo có đủ 3 đáp án sai
                    s.extend(['$1234$', '$5678$', '$9012$']) # Thêm đáp án dự phòng
                    s = list(set(s))
                    if len(s) < 3:
                         s.extend(['$12345$', '$67890$'])
                         s = list(set(s))

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Khi một vận động viên nhảy dù nhảy ra khỏi máy bay, giả sử quãng đường người ấy rơi tự do (tính feet) trong mỗi giây liên tiếp theo thứ tự trước khi bung dù lần lượt là: $%s; %s; %s; \\dots$ (các quãng đường này tạo thành cấp số cộng). Tổng chiều dài quãng đường rơi tự do của người đó trong $%s$ giây đầu tiên bằng bao nhiêu?'''
                                  %(latex(u1),latex(u2),latex(u3),latex(n)
                                  ))

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai=('''Quãng đường rơi tự do trong mỗi giây tạo thành một cấp số cộng với: \\\\
                         - Số hạng đầu $u_1 = %s$ (feet). \\\\
                         - Công sai $d = %s - %s = %s$ (feet). \\\\
                         - Số số hạng $n = %s$ (giây). \\\\
                         Tổng quãng đường rơi tự do trong $%s$ giây đầu tiên là tổng của $%s$ số hạng đầu tiên của cấp số cộng, ký hiệu là $S_{%s}$. \\\\
                         Áp dụng công thức tổng $n$ số hạng đầu: $S_n = \\frac{n \\cdot [2u_1 + (n-1)d]}{2}$ \\\\
                         $$S_{%s} = \\frac{%s \\cdot [2 \\cdot %s + (%s-1) \\cdot %s]}{2} = \\frac{%s \\cdot (%s + %s \\cdot %s)}{2} = \\frac{%s \\cdot %s}{2} = %s \\text{ (feet)}.$$'''
                          %(latex(u1),latex(u2),latex(u1),latex(d),
                            latex(n),latex(n),latex(n),latex(n),
                            latex(n),latex(n),latex(u1),latex(n),latex(d),
                            latex(n),latex(2*u1),latex(n-1),latex(d),
                            latex(n),latex(2*u1 + (n-1)*d),latex(int(Sn))
                          ))
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(int(Sn)))


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('.0', '')
            return content 

