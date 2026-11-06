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


def bt_dang26_p2_b1_c2_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x, y = symbols('x y')

            # Random các thông số cho bài toán
            # Đảm bảo a, b nguyên tố cùng nhau và khác nhau
            a = random.randint(2, 5)
            b = random.randint(2, 5)
            while math.gcd(a, b) != 1 or a == b:
                b = random.randint(2, 5)

            # c là hằng số cho vế phải của bpt ax + by <= c
            c = random.randint(15, 30) * 10 

            # k là hệ số để tạo ra số thập phân cho phí (ví dụ 0.5, 0.6)
            k = random.choice([0.4, 0.5, 0.6, 0.8, 1.2, 1.4, 1.5])

            # Tính toán các phí và giới hạn (làm tròn 2 chữ số để tránh sai số thập phân)
            p1 = round(a * k, 2)
            p2 = round(b * k, 2)
            M = round(c * k, 2)

            # Hàm định dạng số: bỏ số 0 vô nghĩa ở đuôi thập phân và thay dấu chấm bằng phẩy
            def format_num(num):
                if num == int(num):
                    return str(int(num))
                return str(num).replace('.', ',')

            p1_str = format_num(p1)
            p2_str = format_num(p2)
            M_str = format_num(M)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một công ty viễn thông tính phí $%s$ nghìn đồng mỗi phút gọi nội mạng và $%s$ nghìn đồng mỗi phút gọi ngoại mạng. Ông $A$ sử dụng dịch vụ của công ty viễn thông này và mỗi tháng trả số tiền phí không quá $%s$ nghìn đồng. Gọi $x$ là số phút gọi nội mạng, $y$ là số phút gọi ngoại mạng mỗi tháng.'''                  
                             % (p1_str, p2_str, M_str))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Mỗi tháng, số tiền gọi nội mạng là $%sx$ và số tiền gọi ngoại mạng là $%sy$' % (p1_str, p2_str)
            nb_da_1_s = 'Mỗi tháng, số tiền gọi nội mạng là $%sx$ và số tiền gọi ngoại mạng là $%sy$' % (p2_str, p1_str)

            loigiai_nb_d = ('''Vì số phút gọi nội mạng là $x$ nên số tiền tương ứng là $%sx$. \\\\ 
            Số phút gọi ngoại mạng là $y$ nên số tiền tương ứng là $%sy$. \\\\ 
            Mệnh đề đúng.''' % (p1_str, p2_str))

            loigiai_nb_s = ('''Vì số phút gọi nội mạng là $x$ nên số tiền tương ứng là $%sx$. \\\\ 
            Số phút gọi ngoại mạng là $y$ nên số tiền tương ứng là $%sy$. \\\\ 
            Mệnh đề sai.''' % (p1_str, p2_str))

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Bất phương trình bậc nhất hai ẩn $x,y$ trong tình huống trên là $%sx + %sy \\le %s$' % (a, b, c)
            th_da_1_s = 'Bất phương trình bậc nhất hai ẩn $x,y$ trong tình huống trên là $%sx + %sy \\le %s$' % (b, a, c)

            loigiai_th_d = ('''Tổng số tiền phí viễn thông mỗi tháng ông $A$ phải trả là $%sx + %sy$ (nghìn đồng). \\\\
            Vì mỗi tháng ông $A$ trả số tiền phí không quá $%s$ nghìn đồng nên ta có bất phương trình: \\\\
            $%sx + %sy \\le %s \\Leftrightarrow %sx + %sy \\le %s$. \\\\
            Mệnh đề đúng.''' % (p1_str, p2_str, M_str, p1_str, p2_str, M_str, a, b, c))

            loigiai_th_s = ('''Tổng số tiền phí viễn thông mỗi tháng ông $A$ phải trả là $%sx + %sy$ (nghìn đồng). \\\\
            Vì mỗi tháng ông $A$ trả số tiền phí không quá $%s$ nghìn đồng nên ta có bất phương trình: \\\\
            $%sx + %sy \\le %s \\Leftrightarrow %sx + %sy \\le %s$. \\\\
            Mệnh đề sai.''' % (p1_str, p2_str, M_str, p1_str, p2_str, M_str, a, b, c))

            ######################################################################## Vận dụng ############################################
            # Random nghiệm đúng
            x_d = random.randint(1, c // a - 1)
            y_d = random.randint(1, (c - a * x_d) // b)
            val_d = a * x_d + b * y_d

            # Random nghiệm sai
            x_s = random.randint(c // a + 1, c // a + 20)
            y_s = random.randint(c // b + 1, c // b + 20)
            val_s = a * x_s + b * y_s

            # Các đáp án
            vd_da_1_d = '\\True Mỗi tháng ông $A$ có thể gọi $%s$ phút nội mạng và $%s$ phút ngoại mạng' % (x_d, y_d)
            vd_da_1_s = 'Mỗi tháng ông $A$ có thể gọi $%s$ phút nội mạng và $%s$ phút ngoại mạng' % (x_s, y_s)

            loigiai_vd_d = ('''Thay $x = %s, y = %s$ vào vế trái của bất phương trình ta được: \\\\
            $%s \\cdot %s + %s \\cdot %s = %s \\le %s$. \\\\
            Vì số phút trên thỏa mãn điều kiện nên ông $A$ có thể gọi như vậy. \\\\
            Mệnh đề đúng.''' % (x_d, y_d, a, x_d, b, y_d, val_d, c))

            loigiai_vd_s = ('''Thay $x = %s, y = %s$ vào vế trái của bất phương trình ta được: \\\\
            $%s \\cdot %s + %s \\cdot %s = %s > %s$. \\\\
            Vì số phút trên không thỏa mãn điều kiện nên ông $A$ không thể thực hiện được. \\\\
            Mệnh đề sai.''' % (x_s, y_s, a, x_s, b, y_s, val_s, c))

            ######################################################################## Vận dụng cao ############################################
            # Tính diện tích
            dien_tich = Rational(c**2, 2 * a * b)
            dien_tich_sai = Rational(c**2, a * b)

            # Cắt trục tọa độ
            x_int = Rational(c, a)
            y_int = Rational(c, b)

            vdc_da_1_d = '\\True Miền nghiệm của bất phương trình thể hiện số tiền phí viễn thông hàng tháng ông $A$ sử dụng tạo với hai trục tọa độ một tam giác có diện tích bằng $%s$' % latex(dien_tich)
            vdc_da_1_s = 'Miền nghiệm của bất phương trình thể hiện số tiền phí viễn thông hàng tháng ông $A$ sử dụng tạo với hai trục tọa độ một tam giác có diện tích bằng $%s$' % latex(dien_tich_sai)

            loigiai_vdc_d = ('''Vì số phút gọi không thể âm nên $x \\ge 0$ và $y \\ge 0$. \\\\
            Miền nghiệm của hệ giới hạn bởi 2 trục tọa độ và đường thẳng $d: %sx + %sy = %s$. \\\\
            Đường thẳng $d$ cắt trục $Ox$ tại $M\\left( %s; 0 \\right)$ và cắt trục $Oy$ tại $N\\left( 0; %s \\right)$. \\\\
            Đó là một tam giác vuông $OMN$ vuông tại gốc tọa độ $O$. \\\\
            Diện tích của tam giác $OMN$ là: $S = \\frac{1}{2} OM \\cdot ON = \\frac{1}{2} \\cdot %s \\cdot %s = %s$. \\\\
            Mệnh đề đúng.''' % (a, b, c, latex(x_int), latex(y_int), latex(x_int), latex(y_int), latex(dien_tich)))

            loigiai_vdc_s = ('''Vì số phút gọi không thể âm nên $x \\ge 0$ và $y \\ge 0$. \\\\
            Miền nghiệm của hệ giới hạn bởi 2 trục tọa độ và đường thẳng $d: %sx + %sy = %s$. \\\\
            Đường thẳng $d$ cắt trục $Ox$ tại $M\\left( %s; 0 \\right)$ và cắt trục $Oy$ tại $N\\left( 0; %s \\right)$. \\\\
            Đó là một tam giác vuông $OMN$ vuông tại gốc tọa độ $O$. \\\\
            Diện tích của tam giác $OMN$ là: $S = \\frac{1}{2} OM \\cdot ON = \\frac{1}{2} \\cdot %s \\cdot %s = %s \\ne %s$. \\\\
            Mệnh đề sai.''' % (a, b, c, latex(x_int), latex(y_int), latex(x_int), latex(y_int), latex(dien_tich), latex(dien_tich_sai)))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Gom nhóm phương án và lời giải để đồng bộ logic khi xáo trộn
            list_nb = [(nb_da_1_d, loigiai_nb_d), (nb_da_1_s, loigiai_nb_s)]
            list_th = [(th_da_1_d, loigiai_th_d), (th_da_1_s, loigiai_th_s)]
            list_vd = [(vd_da_1_d, loigiai_vd_d), (vd_da_1_s, loigiai_vd_s)]
            list_vdc = [(vdc_da_1_d, loigiai_vdc_d), (vdc_da_1_s, loigiai_vdc_s)]

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                nb = random.choice(list_nb)
                th = random.choice(list_th)
                vd = random.choice(list_vd)
                vdc = random.choice(list_vdc)

                answers = [nb[0], th[0], vd[0], vdc[0]]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lại vào list (Đảm bảo câu hỏi đi kèm đúng với lời giải tương ứng)
            list_nb_1 = [nb[0]]
            list_nb_2 = [nb[1]]

            list_th_1 = [th[0]]
            list_th_2 = [th[1]]

            list_vd_1 = [vd[0]]
            list_vd_2 = [vd[1]]

            list_vdc_1 = [vdc[0]]
            list_vdc_2 = [vdc[1]]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            combined_th = list(zip(list_th_1, list_th_2))
            combined_vd = list(zip(list_vd_1, list_vd_2))
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            random.shuffle(combined_nb)
            random.shuffle(combined_th)
            random.shuffle(combined_vd)
            random.shuffle(combined_vdc)

            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
            str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
                '{'+str(shuffled_answers_nb[0])+'}\n'
                '{'+str(shuffled_answers_th[0])+'}\n'
                '{'+str(shuffled_answers_vd[0])+'}\n'
                '{'+str(shuffled_answers_vdc[0])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

