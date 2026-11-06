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


def bt_dang38_p1_b1_c1_ds10(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Random ngẫu nhiên 4 phương án tương đương để hoán đổi vị trí bản chất
        # Cách random bài này là xáo trộn các cặp mệnh đề và tạo tập hợp mệnh đề đảo ngẫu nhiên

        # Định nghĩa nội dung các mệnh đề gốc và mệnh đề đảo của chúng
        # Mỗi phần tử: (Mệnh đề gốc, Mệnh đề đảo, Trạng thái đảo Đúng/Sai)
        md_A = ('Nếu tổng hai số $a+b > 2$ thì có ít nhất một số lớn hơn $1$', 
                'Nếu hai số $a, b$ có ít nhất một số lớn hơn $1$ thì tổng hai số $a+b > 2$', 
                False) # Sai vì ví dụ a=2, b=-5 thì a+b=-3 < 2

        md_B = ('Trong một tam giác cân, hai đường cao xuất phát từ hai đỉnh đáy bằng nhau', 
                'Nếu một tam giác có hai đường cao bằng nhau thì tam giác đó là tam giác cân', 
                True)  # Đúng (Mệnh đề gốc đúng, mệnh đề đảo cũng đúng)

        md_C = ('Nếu tứ giác là hình vuông thì hai đường chéo vuông góc với nhau', 
                'Nếu một tứ giác có hai đường chéo vuông góc với nhau thì tứ giác đó là hình vuông', 
                False) # Sai vì có thể là hình thoi hoặc hình diều

        md_D = ('Nếu một số tự nhiên chia hết cho $6$ thì nó chia hết cho $3$', 
                'Nếu một số tự nhiên chia hết cho $3$ thì nó chia hết cho $6$', 
                False) # Sai vì số 3, 9 chia hết cho 3 nhưng không chia hết cho 6

        # Lọc ra đáp án đúng (Mệnh đề đảo đúng)
        da_dung_goc = md_B[0]
        da_dung_dao = md_B[1]

        # Danh sách các mệnh đề sai (Mệnh đề đảo sai)
        danh_sach_sai = [md_A, md_C, md_D]
        random.shuffle(danh_sach_sai)

        # Lấy 3 mệnh đề sai
        md_s1 = danh_sach_sai[0][0]
        md_s1_dao = danh_sach_sai[0][1]

        md_s2 = danh_sach_sai[1][0]
        md_s2_dao = danh_sach_sai[1][1]

        md_s3 = danh_sach_sai[2][0]
        md_s3_dao = danh_sach_sai[2][1]

        # Câu hỏi
        noidungcauhoi = ('''Trong các mệnh đề sau, mệnh đề nào có mệnh đề đảo đúng?''')

        # Các đáp án
        da_d = ('\\True ' + str(da_dung_goc))
        da_s1 = str(md_s1)
        da_s2 = str(md_s2) 
        da_s3 = str(md_s3) 

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải chi tiết
        loigiai = ('''Xét mệnh đề đảo của các phương án: \\\\
        - Mệnh đề đảo của phương án có nội dung "%s" là: "%s". Đây là một mệnh đề đúng. \\\\
        - Mệnh đề đảo của phương án có nội dung "%s" là: "%s". Đây là một mệnh đề sai. \\\\
        - Mệnh đề đảo của phương án có nội dung "%s" là: "%s". Đây là một mệnh đề sai. \\\\
        - Mệnh đề đảo của phương án có nội dung "%s" là: "%s". Đây là một mệnh đề sai. \\\\
        Vậy ta chọn phương án có mệnh đề đảo đúng.'''
                        % (str(da_dung_goc), str(da_dung_dao),
                            str(md_s1), str(md_s1_dao),
                            str(md_s2), str(md_s2_dao),
                            str(md_s3), str(md_s3_dao)))

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
        '\\choice \n'
        '{'+str(list_1[1])+'}\n'
        '{'+str(list_1[2])+'}\n'
        '{'+str(list_1[3])+'}\n'
        '{'+str(list_1[0])+'}\n'
        '\\loigiai{'+str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac').replace('++','+').replace('--','+').replace('+-','-').replace('-+','-').replace('10x','10 x').replace('+0x','').replace('-0x','').replace('11x','11 x').replace('1x','x').replace('10y','10 y').replace('+0y','').replace('-0y','').replace('11y','11 y').replace('1y','y').replace('10t','10 t').replace('+0t','').replace('-0t','').replace('11t','11 t').replace('1t','t')
    return content

