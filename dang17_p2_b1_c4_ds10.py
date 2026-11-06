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


def bt_dang17_p2_b1_c4_ds10(self):
            # Khai báo biến
            # Khai báo các thông số cơ bản (có thể random tại đây nếu muốn)
            gia_1 = random.choice([1500,1600,1700,1400])
            gia_2 = random.choice([2000,1900,2100,2200])
            gia_3 = random.choice([3000,2900,3100,3200])
            muc_1 = random.choice([100,90,110,120])
            muc_2 = random.choice([300,290,310,320])

            # Tính toán các hằng số hỗ trợ lời giải
            tien_muc_1 = muc_1 * gia_1
            tien_muc_2 = (muc_2 - muc_1) * gia_2
            tong_1_2 = tien_muc_1 + tien_muc_2

            # Nội dung câu hỏi
            noidungcauhoi = r'''Giả sử giá điện sinh hoạt trong mỗi tháng dành cho các hộ gia đình được cho bởi bảng sau
            \begin{center}
            \begin{tabular}{|c|c|}
            \hline
            Mức kWh điện tiêu thụ & Giá bán điện (VND/ kWh) \\ \hline
            Mức 1: từ $0$ đến %d kWh & $%d$ \\ \hline
            Mức 2: từ trên $%d$ đến $%d$ kWh & $%d$ \\ \hline
            Mức 3: trên $%d$ kWh & $%d$ \\ \hline
            \end{tabular}
            \end{center}''' % (muc_1, gia_1, muc_1, muc_2, gia_2, muc_2, gia_3)

            ########################################################################
            # Nhận biết (Câu a)
            x_a = 50
            tien_a = x_a * gia_1
            nb_da_1_d = r'\True Nếu hộ gia đình tiêu thụ %d kWh thì số tiền phải trả là $%d$ VND' % (x_a, tien_a)
            nb_da_1_s = r'Nếu hộ gia đình tiêu thụ %d kWh thì số tiền phải trả là $%d$ VND' % (x_a, tien_a + 5000)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            loigiai_nb_1 = r'Nếu hộ gia đình tiêu thụ $%d$ kWh thì số tiền phải trả là $%d \cdot %d = %d$ VND.' % (x_a, x_a, gia_1, tien_a)

            ########################################################################
            # Thông hiểu (Câu b)
            he_so_b = gia_2 * muc_1 - tien_muc_1
            th_da_1_d = r'\True Biểu thức biểu diễn số tiền phải trả theo số tiêu thụ điện $x$ là $f(x) = %dx - %d$ (với $%d < x \le %d$)' % (gia_2, he_so_b, muc_1, muc_2)
            th_da_1_s = r'Biểu thức biểu diễn số tiền phải trả theo số tiêu thụ điện $x$ là $f(x) = %dx + %d$' % (gia_2, tien_muc_1)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            loigiai_th_1 = r'''Gọi $x$ kWh là mức điện tiêu thụ. Khi đó, ta có công thức liên hệ giữa số kWh điện tiêu thụ và số tiền tương ứng phải trả $f(x)$ như sau
            $f(x) = \begin{cases} %dx & (0 < x \le %d) \\ %d \cdot %d + %d \cdot (x - %d) & (%d < x \le %d) \\ %d + %d + %d \cdot (x - %d) & (x > %d) \end{cases}$ \\
            $\Leftrightarrow f(x) = \begin{cases} %dx & (0 < x \le %d) \\ %dx - %d & (%d < x \le %d) \\ %dx - %d & (x > %d) \end{cases}$.''' % (
                gia_1, muc_1, gia_1, muc_1, gia_2, muc_1, muc_1, muc_2, tien_muc_1, tien_muc_2, gia_3, muc_2, muc_2,
                gia_1, muc_1, gia_2, he_so_b, muc_1, muc_2, gia_3, muc_2*gia_3 - tong_1_2, muc_2
            )

            ########################################################################
            # Vận dụng (Câu c)
            tien_c = 420000
            x_c = int((tien_c + he_so_b) / gia_2)
            vd_da_1_d = r'\True Số tiền điện một tháng là $%d$ VND thì số điện tiêu thụ là $%d$ kWh' % (tien_c, x_c)
            vd_da_1_s = r'Số tiền điện một tháng là $%d$ VND thì số điện tiêu thụ là $%d$ kWh' % (tien_c, x_c + 10)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            loigiai_vd_1 = r'''Để xác định số tiền điện là $%d$ VND mà hộ gia đình phải trả tương ứng với số kWh điện tiêu thụ bao nhiêu, ta cần xác định công thức tương ứng. \\
            Với $f(x) = %dx, 0 < x \le %d$ thì $0 < f(x) \le %d$. \\
            Với $f(x) = %dx - %d, %d < x \le %d$ thì $%d < f(x) \le %d$. \\
            Vì $%d < %d < %d$ nên ứng với số tiền $%d$ VND thì số kWh điện tiêu thụ của hộ gia đình đó là
            $$\frac{%d + %d}{%d} = %d \text{ kWh.}$$''' % (
                tien_c, gia_1, muc_1, tien_muc_1, gia_2, he_so_b, muc_1, muc_2, tien_muc_1, tong_1_2,
                tien_muc_1, tien_c, tong_1_2, tien_c, tien_c, he_so_b, gia_2, x_c
            )

            ########################################################################
            # Vận dụng cao (Câu d)
            vdc_da_1_d = r'\True Số tiền điện một tháng tối đa để không vượt quá mức $2$ là $%d$ VND' % (tong_1_2)
            vdc_da_1_s = r'Số tiền điện một tháng tối đa để không vượt quá mức $2$ là $%d$ VND'% (tong_1_2+100000)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            loigiai_vdc_1 = r'Số tiền điện một tháng tối đa để không vượt quá mức $2$ là $%d$ VND.' % (tong_1_2)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Xuất nội dung theo mẫu content
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
                '{'+str(nb_da_1)+'}\n'
                '{'+str(th_da_1)+'}\n'
                '{'+str(vd_da_1)+'}\n'
                '{'+str(vdc_da_1)+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(loigiai_nb_1)+'\n'
                '\\item '+str(loigiai_th_1)+'\n'
                '\\item '+str(loigiai_vd_1)+'\n'
                '\\item '+str(loigiai_vdc_1)+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

