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


def bt_dang30_p3_b1_c4_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random dữ liệu đầu vào để tạo đề mới
                xe_list = ["Mercedes S450", "Toyota Camry", "Honda Accord", "Mazda 6", "VinFast Lux A2.0", "Hyundai Santa Fe"]
                xe = random.choice(xe_list)

                prefix_list = ["29E", "30A", "30E", "29A", "30F", "29C", "51G", "51H"]
                prefix = random.choice(prefix_list)

                # Chỉ có 0 và 5 là đứng đơn lẻ (không có cặp tổng = 10 trong các chữ số phân biệt từ 0-9)
                chuso = random.choice([0, 5])
                chuso_conlai = 5 if chuso == 0 else 0

                # Kết quả xác suất (không đổi do bản chất tập hợp tổ hợp giữ nguyên)
                kq = '0,38'

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (kq)]
                da = random.choice(du)

                s = ['$0,39$', '$0,37$', '$0,41$', '$0,42$', '$0,36$', '$0,35$', '$0,40$']

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Anh Đạt mới mua một chiếc xe ô tô nhãn hiệu %s. Sau quá trình bấm biển số thì biển số xe có dạng %s - $abcde$ với $a,b,c,d,e$ là các chữ số phân biệt từ 0 đến 9. Chiếc biển xe của anh Đạt được coi là biển xe "may mắn" nếu không có hai chữ số nào có tổng bằng 10. Hãy tính xác suất để anh Đạt bấm được một biển xe "may mắn", biết rằng biển số đó có chứa chữ số %s (Kết quả làm tròn đến hàng phần trăm).'''
                                 % (xe, prefix, chuso))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Tìm số lượng các biển số có 5 chữ số đôi một khác nhau lập từ tập $S=\\{0;1;2;...;9\\}$ mà trong đó bắt buộc có chữ số $%s$. \\\\
            Gọi $A$ là biến cố "Biển số xe may mắn" và $B$ là biến cố "Biển số xe có chữ số $%s$". \\\\
            Tổng số biển có 5 chữ số khác nhau $A_{10}^5$. \\\\
            Số biển không chứa chữ số $%s$ là $A_9^5$ nên $n(B)=A_{10}^5 - A_9^5 = 15120$ (biển). \\\\
            Các cặp số có tổng bằng 10 là: $\\{1;9\\}, \\{2;8\\}, \\{3;7\\}, \\{4;6\\}$. \\\\
            \\textbf{Trường hợp 1:} Chọn số $%s$ \\\\
            Bộ số hiện có $\\{%s;%s\\}$ thì ta cần chọn thêm 3 số nữa được lấy từ $\\{1;9\\}, \\{2;8\\}, \\{3;7\\}, \\{4;6\\}$ (mỗi nhóm 1 số). \\\\
            Chọn 3 nhóm từ 4 nhóm có $C_4^3=4$ (cách). \\\\
            Trong mỗi nhóm đã chọn, có 2 cách chọn một số nên có: $2 \\cdot 2 \\cdot 2 = 8$ (cách chọn). \\\\
            Xếp 5 số này vào 5 vị trí có $5!$ (cách). \\\\
            Số biển thỏa mãn cho trường hợp này là: $4 \\cdot 8 \\cdot 5! = 3840$ (biển). \\\\
            \\textbf{Trường hợp 2:} Không chọn số $%s$ \\\\
            Bộ số hiện có là $\\{%s\\}$ thì ta cần chọn thêm 4 số nữa từ $\\{1;9\\}, \\{2;8\\}, \\{3;7\\}, \\{4;6\\}$ (mỗi nhóm 1 số) và 4 số này phải lấy từ cả 4 nhóm nên có 1 cách chọn. \\\\
            Trong mỗi nhóm, có hai cách chọn 1 số nên có $2 \\cdot 2 \\cdot 2 \\cdot 2 = 16$ (cách). \\\\
            Số cách chọn bộ số là $1 \\cdot 16 = 16$ (cách). \\\\
            Xếp 5 số này vào 5 vị trí có $5!$ (cách). \\\\
            Số biển thỏa mãn cho trường hợp này là: $16 \\cdot 5! = 1920$ (biển). \\\\
            Tổng số biển cố thuận lợi là: $n(A \\cap B) = 3840 + 1920 = 5760$. \\\\
            Vậy xác suất cần tính là: $P(A|B) = \\frac{n(A \\cap B)}{n(B)} = \\frac{5760}{15120} = \\frac{8}{21} \\approx 0,38$.'''
                         % (chuso, chuso, chuso, chuso_conlai, chuso, chuso_conlai, chuso_conlai, chuso))
                dapan='\\shortans[0]{$%s$}\n'%(0.38)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n\\end{minipage} \n\n')
            return content

