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


def bt_dang7_p4_b2_c3_ds10(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                x1=randint(1,20)
                x2=randint(1,20)
                x3=randint(1,20)
                x4=randint(1,20)
                x5=randint(1,20)
                x6=randint(1,20)
                x7=randint(1,20)
                x8=randint(1,20)
                x9=randint(1,20)
                x10=randint(1,20)

                xtb = Decimal(float((x1+x2+x3+x4+x5+x6+x7+x8+x9+x10)/10)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

                # Đưa các số vào danh sách
                numbers = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10]

                # Sắp xếp danh sách theo thứ tự tăng dần
                numbers.sort()

                # Tìm hai số đứng giữa
                x_5 = numbers[4]
                x_6 = numbers[5]
                me=(x_5+x_6)/2

                x_3 = numbers[2]
                q1=x_3 

                x_8 = numbers[7]
                q3=x_8  

                #Tìm mốt
                # Đếm số xuất hiện
                counter = Counter(numbers)

                while counter==10:
                    x1=randint(1,20)
                    x2=randint(1,20)
                    x3=randint(1,20)
                    x4=randint(1,20)
                    x5=randint(1,20)
                    x6=randint(1,20)
                    x7=randint(1,20)
                    x8=randint(1,20)
                    x9=randint(1,20)
                    x10=randint(1,20)

                # Tìm số xuất hiện nhiều nhất
                max_count = max(counter.values())
                most_common_numbers = [num for num, count in counter.items() if count == max_count]

                gia_tri=most_common_numbers
                so_lan=max_count

                # Tính tổng các số xuất hiện nhiều nhất
                most_common_sum = sum(most_common_numbers)

                # Lấy 3 số bất kỳ không phải là mốt
                other_numbers = [num for num in numbers if num not in most_common_numbers]
                if len(other_numbers) >= 3:
                    random_numbers = sample(other_numbers, 3)  # Lấy 3 số ngẫu nhiên
                else:
                    random_numbers = other_numbers  # Lấy tất cả nếu không đủ 3 số

                # Gán 3 số đó vào x1, x2, x3
                if len(random_numbers) >= 3:
                    m1, m2, m3 = random_numbers[:3]
                else:
                    m1, m2, m3 = (random_numbers + [None, None, None])[:3]  # Gán None nếu thiếu số


                # Nội dung câu hỏi
                noidungcauhoi = ('Cho mẫu số liệu \n'
                                '$$%s\\hspace*{0.5cm} %s\\hspace*{0.5cm} %s\\hspace*{0.5cm} %s\\hspace*{0.5cm} %s\\hspace*{0.5cm} %s\\hspace*{0.5cm} %s\\hspace*{0.5cm} %s\\hspace*{0.5cm} %s\\hspace*{0.5cm} %s$$'
                                'Tìm tổng các mốt của mẫu số liệu.'

                                %(latex(x1),latex(x2),latex(x3),latex(x4),latex(x5),latex(x6),latex(x7),latex(x8),latex(x9),latex(x10)
                                ))

                # Nội dung lời giải
                loigiai=('Xắp xếp dãy số theo thứ tự tăng dần ta được \\\\ \n'
                        '$$%s$$ \n'
                        'Giá trị $%s$ xuất hiện nhiều nhất $%s$ lần nên mốt của dãy số liệu là $%s$. \\\\ \n'
                        'Suy ra tổng các mốt của dãy số liệu là $%s$.'

                        %(latex(numbers),
                        latex(gia_tri),latex(so_lan),latex(gia_tri),
                        latex(most_common_sum)


                        ))


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('\\left[', '').replace('\\right]', '').replace(',0$', '$').replace(', \\', '\\hspace*{0.5cm}')
            return content

