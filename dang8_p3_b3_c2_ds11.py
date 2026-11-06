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


def bt_dang8_p3_b3_c2_ds11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Khai báo biến ngẫu nhiên
                u1 = randint(20, 100) # Lượng thuốc ngày đầu (mg)

                # Chọn ngẫu nhiên công bội q (0 < q < 1)
                # Cặp tử số/mẫu số: (1/2), (1/3), (2/3), (1/4), (3/4), (2/5), ...
                q_pairs = [(1, 2), (1, 3), (2, 3), (1, 4)] 
                q_pair = random.choice(q_pairs)
                q = Rational(q_pair[0], q_pair[1])

                # Mô tả công bội
                if q == Rational(1, 2):
                    q_text = 'một nửa'
                elif q == Rational(1, 3):
                    q_text = 'một phần ba'
                elif q == Rational(2, 3):
                    q_text = 'hai phần ba'
                elif q == Rational(1, 4):
                    q_text = 'một phần tư'
                else:
                    q_text = '%s phần %s'%(q_pair[0], q_pair[1])

                n = randint(8, 15) # Số ngày liên tiếp

                # Tính toán
                # S_n = u1 * (1 - q**n) / (1 - q)
                Sn_exact = u1 * (1 - q**n) / (1 - q)

                # Làm tròn kết quả đến 3 chữ số thập phân
                kq2 = round(float(Sn_exact), 0) 

                # Chuyển đổi sang định dạng hiển thị (dấu phẩy)
                kq = str(kq2).replace('.0', '') 

                # Đáp án đúng
                da = '$%s \\ (mg)$'%(kq)

                # Các đáp án trắc nghiệm sai (sử dụng các giá trị làm tròn khác nhau)
                s = ['$%s \\ (mg)$'%(str(round(kq2 + 0.1, 0)).replace('.0', '')), 
                     '$%s \\ (mg)$'%(str(round(kq2 - 0.1, 0)).replace('.0', '')), 
                     '$%s \\ (mg)$'%(str(round(u1 * n, 0)).replace('.0', '')), # Tổng không giảm (nhiễu sai)
                     '$%s \\ (mg)$'%(str(round(u1 * 2, 0)).replace('.0', '')) # 2 lần liều đầu (nhiễu sai)
                    ]

                # Thêm 3 đáp án sai từ danh sách
                random.shuffle(s)
                das1 = s.pop()
                das2 = s.pop()
                das3 = s.pop()


                # Câu hỏi
                noidungcauhoi = ('''Một loại thuốc được dùng mỗi ngày một lần. Lúc đầu nồng độ thuốc trong máu của bệnh nhân
                tăng nhanh, nhưng mỗi liều kế tiếp có tác dụng ít hơn liều trước đó. Lượng thuốc trong máu ở
                ngày thứ nhất là $%s\\text{mg}$, và mỗi ngày sau đó giảm chỉ còn $%s$ so với liều trước đó.
                Tổng lượng thuốc (tính bằng \\text{mg}) trong máu của bệnh nhân sau khi dùng thuốc $%s$ ngày liên tiếp bằng bao nhiêu? (làm tròn kết quả đến hàng đơn vị).'''
                %(latex(u1), q_text, latex(n)))

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai=('''Lượng thuốc trong máu mỗi ngày bệnh nhân nhận là thành phần của một cấp số nhân với:
                \\\\
                Số hạng đầu: $u_1 = %s\\text{mg}$. \\\\
                Công bội: $q = %s$. \\\\
                \\\\
                Tổng lượng thuốc trong máu sau $%s$ ngày liên tiếp chính là tổng $%s$ số hạng đầu của cấp số nhân này,
                được tính theo công thức: $S_n = u_1 \\frac{1 - q^n}{1 - q}$.
                \\\\
                Thay số:
                $$S_{%s} = %s \\cdot \\frac{1 - (%s)^{%s}}{1 - %s} \\approx %s\\text{ (mg).}$$'''
                %(latex(u1),
                  latex(q),
                  latex(n), latex(n),
                  latex(n), latex(u1), latex(q), latex(n), latex(q), kq))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

