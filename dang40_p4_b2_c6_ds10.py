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


def bt_dang40_p4_b2_c6_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Suy nghĩ tìm cách random bài toán
                n1 = randint(2, 4) # Góc phần tư thứ nhất
                n2 = randint(3, 5) # Góc phần tư thứ hai
                n3 = randint(4, 6) # Góc phần tư thứ ba
                n4 = randint(5, 7) # Góc phần tư thứ tư

                tong_diem = n1 + n2 + n3 + n4

                # Tính số phần tử không gian mẫu sử dụng math.comb
                omega = int(math.comb(tong_diem, 2))

                # Tính số phần tử của biến cố A
                na_1_3 = n1 * n3
                na_2_4 = n2 * n4
                na = na_1_3 + na_2_4

                # Đáp án đúng
                kq_phanso = Rational(na, omega)
                da = '$%s$' % (latex(kq_phanso))

                # Bước 4: Tạo các phương án sai
                s_list = []
                sai_1 = Rational(na_1_3, omega)
                sai_2 = Rational(na_2_4, omega)
                sai_3 = Rational(na + 1, omega)
                sai_4 = Rational(na - 1, omega)

                potential_wrongs = [sai_1, sai_2, sai_3, sai_4]
                for sw in potential_wrongs:
                    if sw != kq_phanso and sw > 0:
                        s_list.append('$%s$' % (latex(sw)))

                s_list = list(set(s_list))
                while len(s_list) < 3:
                    random_val = Rational(randint(5, 80), omega)
                    if random_val != kq_phanso:
                        s_list.append('$%s$' % (latex(random_val)))

                das1 = random.choice(s_list)
                s_list.remove(das1)
                das2 = random.choice(s_list)
                s_list.remove(das2)
                das3 = random.choice(s_list)

                # Câu hỏi
                noidungcauhoi = ('''Trong mặt phẳng tọa độ $Oxy$. Ở góc phần tư thứ nhất ta lấy $%s$ điểm phân biệt, cứ thế ở góc phần tư thứ hai, ba, tư lần lượt lấy $%s, %s, %s$ điểm phân biệt (các điểm không nằm trên các trục tọa độ). Trong $%s$ điểm đó ta lấy hai điểm bất kì. Tính xác suất để đoạn thẳng nối hai điểm đó cắt hai trục tọa độ.'''
                                 % (latex(n1), latex(n2), latex(n3), latex(n4), latex(tong_diem)))

                da_d = '\\True ' + str(da)
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Lời giải chi tiết
                loigiai = ('''Số phần tử của không gian mẫu là $n\\left(\\Omega\\right) = C_{%s}^{2} = %s$. \\\\
                            Gọi $A$ là biến cố "đoạn thẳng nối hai điểm đó cắt hai trục tọa độ". \\\\
                            Đoạn thẳng nối hai điểm đó cắt hai trục tọa độ thì hai đầu đoạn thẳng đó phải nằm ở góc phần tư thứ nhất và thứ ba, hoặc góc phần tư thứ hai và thứ tư. \\\\
                            - Hai đầu đoạn thẳng ở góc phần tư thứ nhất và thứ ba có $C_{%s}^{1}C_{%s}^{1} = %s$ cách. \\\\
                            - Hai đầu đoạn thẳng ở góc phần tư thứ hai và thứ tư có $C_{%s}^{1}C_{%s}^{1} = %s$ cách. \\\\
                            Số phần tử của biến cố $A$ là $n\\left(A\\right) = C_{%s}^{1}C_{%s}^{1} + C_{%s}^{1}C_{%s}^{1} = %s$. \\\\
                            Vậy xác suất cần tính là $P\\left(A\\right) = \\frac{%s}{%s} = %s$.'''
                           % (latex(tong_diem), latex(omega),
                              latex(n1), latex(n3), latex(na_1_3),
                              latex(n2), latex(n4), latex(na_2_4),
                              latex(n1), latex(n3), latex(n2), latex(n4), latex(na),
                              latex(na), latex(omega), latex(kq_phanso)))

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + 
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

