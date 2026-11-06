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


def bt_dang14_p3_b3_c6_ds11(self):
            # Khai báo biến
            # B1 & B3: Nghiên cứu đề bài và thiết lập các biến số ngẫu nhiên
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Tạo ngẫu nhiên các xác suất thành công cho 5 cầu thủ (p1 -> p5)
                # Lấy các giá trị xung quanh giá trị của đề bài để đảm bảo tính thực tế
                p1 = random.choice([0.7, 0.75, 0.8, 0.85, 0.9])
                p2 = random.choice([0.7, 0.75, 0.8, 0.85, 0.9])
                p3 = random.choice([0.6, 0.65, 0.7, 0.76, 0.8])
                p4 = random.choice([0.6, 0.7, 0.72, 0.75, 0.8])
                p5 = random.choice([0.65, 0.68, 0.7, 0.75, 0.8])

                # Xác suất thất bại của cầu thủ cuối cùng
                q5 = 1 - p5

                # Tính xác suất: Chỉ cầu thủ cuối cùng sút trượt
                # P = P(A1) * P(A2) * P(A3) * P(A4) * P(not A5)
                kq_chinh_xac = p1 * p2 * p3 * p4 * q5

                # Làm tròn đến hàng phần mười theo quy tắc ROUND_HALF_UP
                kq_decimal = Decimal(str(kq_chinh_xac)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Định dạng hiển thị dấu phẩy cho số thập phân
                kq_str = str(kq_decimal).replace('.', ',')
                p1_s = str(p1).replace('.', ',')
                p2_s = str(p2).replace('.', ',')
                p3_s = str(p3).replace('.', ',')
                p4_s = str(p4).replace('.', ',')
                p5_s = str(p5).replace('.', ',')
                q5_s = str(round(q5, 2)).replace('.', ',')

                # B4: Tạo các phương án sai không trùng với đáp án đúng
                da = '$' + kq_str + '$'

                s_list = []
                current_val = float(kq_decimal)
                # Tạo các giá trị sai lệch 0,1; 0,2; 0,3...
                for i in [-0.3, -0.2, -0.1, 0.1, 0.2, 0.3]:
                    sai_val = round(current_val + i, 1)
                    if sai_val >= 0 and sai_val != current_val:
                        s_list.append('$' + str(sai_val).replace('.', ',') + '$')

                random.shuffle(s_list)
                das1 = s_list[0]
                das2 = s_list[1]
                das3 = s_list[2]

                # B2: Nội dung câu hỏi theo mẫu
                noidungcauhoi = ('Trong một trận đấu bóng đá quan trọng ở vòng đấu loại trực tiếp, khi trận đấu buộc phải giải quyết bằng loạt sút luân lưu $11m$, huấn luyện viên đội $X$ đưa danh sách lần lượt $5$ cầu thủ có xác suất sút luân lưu $11m$ thành công là $%s;%s;%s;%s;%s$. Xác suất để chỉ có cầu thủ cuối cùng sút trượt luân lưu bằng bao nhiêu? (kết quả làm tròn đến hàng phần mười).'
                                 % (p1_s, p2_s, p3_s, p4_s, p5_s))

                # Các đáp án
                da_d = '\\True ' + str(da)
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết (không viết tắt, dùng \left \right)
                loigiai = ('Gọi $A_i \\left( 1 \\leq i \\leq 5, i \\in \\mathbb{N} \\right)$ là biến cố: "Cầu thủ thứ $i$ của đội $X$ sút luân lưu thành công". \\\\ '
                           'Xác suất cần tìm là: \\\\ '
                           '$P\\left( A_1 A_2 A_3 A_4 \\bar{A}_5 \\right) = P\\left( A_1 \\right) \\cdot P\\left( A_2 \\right) \\cdot P\\left( A_3 \\right) \\cdot P\\left( A_4 \\right) \\cdot P\\left( \\bar{A}_5 \\right)$ \\\\ '
                           '$= %s \\cdot %s \\cdot %s \\cdot %s \\cdot %s \\approx %s$.'
                           % (p1_s, p2_s, p3_s, p4_s, q5_s, kq_str))
                dapan=' \\shortans[0]{$%s$} '%(kq_str) 
            # Xuất câu trắc nghiệm theo định dạng yêu cầu (không dùng tiền tố r)
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content  

