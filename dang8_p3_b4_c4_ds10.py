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


def bt_dang8_p3_b4_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Thiết lập bộ số gốc: AC=120, BC=350, AB=370. AD=130, BD=300. 
                # v1=13, v2=15, t=30. Kết quả CD=50, x=10.
                # Sử dụng hệ số k để random số liệu
                k = random.randint(1, 3)

                AC_val = 120 * k
                AB_val = 370 * k
                BC_val = 350 * k # sqrt(370^2 - 120^2)

                v1 = 13 * k
                v2 = 15 * k
                T_total = 30

                # Kết quả x (thời gian trên AD) luôn là 10 giây với bộ số này
                x_val = 10
                AD_val = v1 * x_val
                BD_val = v2 * (T_total - x_val)
                CD_val = BC_val - BD_val

                # Đáp án đúng
                kq = CD_val
                da = '$%s$m' % (latex(kq))

                # Các đáp án nhiễu
                s = [
                    '$%s$m' % (latex(kq + 10)),
                    '$%s$m' % (latex(kq + 20)),
                    '$%s$m' % (latex(kq - 10)),
                    '$%s$m' % (latex(kq + 5)),
                    '$%s$m' % (latex(kq - 5)),
                    '$%s$m' % (latex(kq + 15))
                ]

                # Chọn ngẫu nhiên 3 đáp án sai từ danh sách s
                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Một chú thỏ ngày nào cũng ra bờ suối ở vị trí $A$, cách cửa hang của mình tại vị trí $B$ là $%s$m để uống nước, sau đó chú thỏ sẽ đến vị trí $C$ cách vị trí $A$ là $%s$m để ăn cỏ rồi trở về hang. Tuy nhiên, hôm nay sau khi uống nước ở bờ suối, chú thỏ không đến vị trí $C$ như mọi ngày mà chạy đến vị trí $D$ để tìm cà rốt rồi mới trở về hang. Biết rằng, tổng thời gian chú thỏ chạy từ vị trí $A$ đến vị trí $D$ rồi về hang là $%s$ giây (không kể thời gian tìm cà rốt), trên đoạn $AD$ chú thỏ chạy với vận tốc là $%s$m/s, trên đoạn $BD$ chú thỏ chạy với vận tốc là $%s$m/s. Khoảng cách giữa hai vị trí $C$ và $D$ bằng bao nhiêu?'''
                                 % (latex(AB_val), latex(AC_val), latex(T_total), latex(v1), latex(v2)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào danh sách và trộn
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Gọi thời gian chú thỏ chạy trên đoạn $AD$ là $x (0 < x < %s)$ (giây), khi đó thời gian chú thỏ chạy trên đoạn $BD$ là $%s - x$ (giây). \\\\
            Do đó, quãng đường $AD$ và $BD$ lần lượt là $%sx$ (m) và $%s(%s - x)$ (m). \\\\
            Độ dài quãng đường $BC$ là: $\\sqrt{%s^2 - %s^2} = %s$ (m). \\\\
            Tam giác $ACD$ vuông tại $C$ nên $CD = \\sqrt{(%sx)^2 - %s^2}$ (m). \\\\
            Mặt khác, $CD = BC - BD = %s - %s(%s - x)$ (m). \\\\
            Do đó, ta có phương trình: $\\sqrt{(%sx)^2 - %s^2} = %s - %s(%s - x)$. \\\\
            Giải phương trình này và kết hợp với điều kiện $0 < x < %s$, ta nhận $x = %s$ (giây). \\\\
            Vậy khoảng cách giữa vị trí $C$ và vị trí $D$ là: $%s - %s(%s - %s) = %s$ (m).'''
                           % (latex(T_total), latex(T_total), 
                              latex(v1), latex(v2), latex(T_total),
                              latex(AB_val), latex(AC_val), latex(BC_val),
                              latex(v1), latex(AC_val),
                              latex(BC_val), latex(v2), latex(T_total),
                              latex(v1), latex(AC_val), latex(BC_val), latex(v2), latex(T_total),
                              latex(T_total), latex(x_val),
                              latex(BC_val), latex(v2), latex(T_total), latex(x_val), latex(kq)
                             ))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

