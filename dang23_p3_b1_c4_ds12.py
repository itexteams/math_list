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


def bt_dang23_p3_b1_c4_ds12(self):
            # Khai báo biến
            # Khai báo danh sách dạng bài
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Suy nghĩ tìm cách random bài toán
                # p_bus: Xác suất chọn xe buýt (%), p_bike: Xác suất chọn xe đạp (%)
                # m_bus: Xác suất muộn khi đi xe buýt (%), m_bike: Xác suất muộn khi đi xe đạp (%)

                p_bus = random.choice([40, 50, 60]) 
                p_bike = 100 - p_bus

                m_bus = randint(5, 12)
                m_bike = randint(2, 8)

                # Tính toán giá trị số thực
                P_B = p_bus / 100
                P_notB = p_bike / 100
                P_M_B = m_bus / 100
                P_M_notB = m_bike / 100

                # Công thức xác suất đầy đủ: P(M) = P(B).P(M|B) + P(B_).P(M|B_)
                kq_val = P_B * P_M_B + P_notB * P_M_notB

                # Làm tròn đến hàng phần trăm (2 chữ số thập phân)
                kq_fixed = Decimal(str(kq_val)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                kq = str(kq_fixed).replace('.', ',')

                # Bước 4: Điều chỉnh các phương án sai không được trùng đáp án đúng
                # Tạo các phương án nhiễu quanh đáp án đúng
                s_set = set()
                while len(s_set) < 3:
                    sai_val = float(kq_fixed) + random.choice([-0.02, -0.01, 0.01, 0.02, 0.03])
                    if sai_val > 0 and sai_val != float(kq_fixed):
                        sai_str = '$%s$' % (str(Decimal(str(sai_val)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ','))
                        s_set.add(sai_str)

                s = list(s_set)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                da_dung = '$%s$' % (kq)

                # Nội dung câu hỏi
                # Nếu p_bus = 50 thì dùng cụm từ "ngẫu nhiên một trong hai... với xác suất như nhau"
                if p_bus == 50:
                    mo_dau = "An chọn ngẫu nhiên một trong hai phương tiện này với xác suất như nhau (tức là 50\\% đi xe buýt, 50\\% đi xe đạp)."
                else:
                    mo_dau = "Xác suất An chọn đi xe buýt là %s\\%% và đi xe đạp là %s\\%%." % (p_bus, p_bike)

                noidungcauhoi = ("Bạn An đi học mỗi ngày bằng một trong hai phương tiện: xe buýt hoặc xe đạp. Vì vội, " + mo_dau + 
                                 " Nếu An đi xe buýt thì xác suất bị muộn học là %s\\%%; nếu An đi xe đạp thì xác suất bị muộn học là %s\\%%. "
                                 "Hỏi vào một ngày bất kỳ, xác suất An bị muộn học là bao nhiêu? (làm tròn kết quả đến hàng phần trăm)." 
                                 % (m_bus, m_bike))

                # Các đáp án
                da_d = ('\\True ' + str(da_dung))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Bước 2: Viết lại lời giải chi tiết giống nội dung trong ảnh
                loigiai = ("Gọi biến cố $B$: “An đi xe buýt”; $\\overline{B}$: “An đi xe đạp”; $M$: “An đi học muộn”. \\\\ "
                           "Xác suất An đi xe buýt $P(B) = %s$. \\\\ "
                           "Xác suất An đi xe đạp $P(\\overline{B}) = %s$. \\\\ "
                           "Do xác suất An đi học muộn khi đi xe buýt là %s\\%% nên $P(M | B) = %s$. \\\\ "
                           "Do xác suất An đi học muộn khi đi xe đạp là %s\\%% nên $P(M | \\overline{B}) = %s$. \\\\ "
                           "Xác suất An bị muộn học là \\\\ "
                           "$P(M) = P(B).P(M | B) + P(\\overline{B}).P(M | \\overline{B}) = %s \\cdot %s + %s \\cdot %s = %s$." 
                           % (str(P_B).replace('.', ','), str(P_notB).replace('.', ','), 
                              m_bus, str(P_M_B).replace('.', ','), 
                              m_bike, str(P_M_notB).replace('.', ','),
                              str(P_B).replace('.', ','), str(P_M_B).replace('.', ','),
                              str(P_notB).replace('.', ','), str(P_M_notB).replace('.', ','),
                              kq))
                dapan=' \\shortans[0]{$%s$} '%(kq)
            # Xuất câu trắc nghiệm (Phần content không dùng tiền tố r)
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

