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


def bt_dang15_p3_b1_c5_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 3: Random bài toán (Thay đổi số lượng các đồ vật)
                n1 = randint(5, 12)  # Số cây bút chì
                n2 = randint(4, 10)  # Số cây bút bi
                n3 = randint(10, 20) # Số cuốn tập

                # Kết quả đúng theo quy tắc cộng
                kq = n1 + n2 + n3

                # Các đáp án trắc nghiệm
                da = '$%s$' % (latex(kq))

                # Bước 4: Tạo các phương án sai và kiểm tra không trùng với đáp án đúng
                # s1: Quy tắc nhân (nếu học sinh nhầm)
                # s2, s3, s4: Các tổng thiếu hoặc sai lệch
                sai_1 = n1 * n2 * n3
                sai_2 = n1 + n2
                sai_3 = n1 + n3
                sai_4 = n1 + n2 + n3 + 2
                sai_5 = abs(n1 + n2 - n3)

                s = [
                    '$%s$' % (latex(sai_1)),
                    '$%s$' % (latex(sai_2)),
                    '$%s$' % (latex(sai_3)),
                    '$%s$' % (latex(sai_4)),
                    '$%s$' % (latex(sai_5)),
                    '$%s$' % (latex(kq + 5))
                ]

                # Loại bỏ giá trị trùng với đáp án đúng trong danh sách phương án sai
                s = [x for x in s if x != da]
                # Chọn ngẫu nhiên 3 đáp án sai từ danh sách đã lọc
                wrong_choices = random.sample(s, 3)

                das1 = wrong_choices[0]
                das2 = wrong_choices[1]
                das3 = wrong_choices[2]

                # Bước 2: Viết lại nội dung câu hỏi theo mẫu
                noidungcauhoi = ('''Trên bàn có $%s$ cây bút chì khác nhau, $%s$ cây bút bi khác nhau và $%s$ cuốn tập khác nhau. Một học sinh muốn chọn một đồ vật duy nhất hoặc một cây bút chì hoặc một cây bút bi hoặc một cuốn tập thì số cách chọn khác nhau bằng bao nhiêu?'''
                                %(latex(n1), latex(n2), latex(n3)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết (không viết tắt)
                loigiai = ('''Nếu chọn một cây bút chì thì sẽ có $%s$ cách. \\\\
                            Nếu chọn một cây bút bi thì sẽ có $%s$ cách. \\\\
                            Nếu chọn một cuốn tập thì sẽ có $%s$ cách. \\\\
                            Theo quy tắc cộng, ta có $%s + %s + %s = %s$ cách chọn.'''
                          %(latex(n1), latex(n2), latex(n3), latex(n1), latex(n2), latex(n3), latex(kq)))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))

            # Xuất câu trắc nghiệm theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

