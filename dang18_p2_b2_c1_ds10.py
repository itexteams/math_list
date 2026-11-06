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


def bt_dang18_p2_b2_c1_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x_sym=symbols('x')

            # Random các thông số cho bài toán sao cho luôn có nghiệm nguyên và duy nhất
            while True:
                c = random.randint(1, 3)
                nbc = random.randint(1, 4)
                a = nbc + 3 * c
                b = a - c
                x_val = random.randint(2, a - 1)
                m = a - x_val
                S = a + b + c + nbc + x_val
                if 15 <= S <= 35 and (S + m) <= 35:
                    break

            # Nội dung câu hỏi
            noidungcauhoi = ('''Trong đợt quyên góp ủng hộ đồng bào bị lũ lụt, có %s học sinh lớp 12A đã tham gia ủng hộ, mỗi học sinh ủng hộ nhiều nhất 2 tờ tiền khác nhau trong ba loại tờ tiền mệnh giá 5.000 đồng, 10.000 đồng và 20.000 đồng. Biết rằng số học sinh đã tham gia ủng hộ thỏa đồng thời ba kết quả sau:\\\\
            - Số học sinh chỉ ủng hộ một tờ 5.000 đồng bằng tổng số học sinh chỉ ủng hộ một tờ 10.000 đồng và số học sinh chỉ ủng hộ một tờ 20.000 đồng.\\\\
            - Trong số học sinh không ủng hộ tờ 5.000 đồng thì số học sinh có ủng hộ tờ 10.000 đồng nhiều gấp hai lần số học sinh có ủng hộ tờ 20.000 đồng.\\\\
            - Số học sinh chỉ ủng hộ một tờ 5.000 đồng nhiều hơn số học sinh ủng hộ tờ 5.000 đồng và một tờ khác là %s học sinh.\\\\
            Xét tính đúng sai của các khẳng định sau:''' 
                             % (S, m))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nbc_s = nbc + random.choice([-1, 1, 2])
            if nbc_s <= 0: nbc_s = nbc + 1

            nb_da_1_d = '\\True Có %s học sinh ủng hộ một tờ 10.000 đồng và một tờ 20.000 đồng' % (nbc)
            nb_da_1_s = 'Có %s học sinh ủng hộ một tờ 10.000 đồng và một tờ 20.000 đồng' % (nbc_s)
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Gọi $x_1, x_2, x_3$ lần lượt là số học sinh chỉ ủng hộ một tờ 5.000 đồng, 10.000 đồng và 20.000 đồng.\\\\
            Gọi $x_{12}, x_{13}, x_{23}$ lần lượt là số học sinh ủng hộ hai tờ (5.000, 10.000), (5.000, 20.000) và (10.000, 20.000).\\\\
            Theo giả thiết, ta có hệ phương trình:\\\\
            $\\begin{cases} 
            x_1 + x_2 + x_3 + x_{12} + x_{13} + x_{23} = %s \\quad (1) \\\\ 
            x_1 = x_2 + x_3 \\quad (2) \\\\ 
            x_2 + x_{23} = 2(x_3 + x_{23}) \\quad (3) \\\\ 
            x_1 = (x_{12} + x_{13}) + %s \\quad (4) 
            \\end{cases}$ \\\\
            Từ (3) suy ra $x_{23} = x_2 - 2x_3$.\\\\
            Thay (2) vào (1) ta được: $2x_1 + x_{23} + (x_{12} + x_{13}) = %s$.\\\\
            Kết hợp với (4), ta có $2x_1 + x_{23} + x_1 - %s = %s \\Leftrightarrow 3x_1 + x_{23} = %s$.\\\\
            Mặt khác, $x_{23} = x_2 - 2x_3 = (x_1 - x_3) - 2x_3 = x_1 - 3x_3$.\\\\
            Nên $3x_1 + (x_1 - 3x_3) = %s \\Leftrightarrow 4x_1 - 3x_3 = %s \\Rightarrow x_3 = \\frac{4x_1 - %s}{3}$.\\\\
            Vì $x_3 \\ge 0$ nên $4x_1 - %s \\ge 0 \\Rightarrow x_1 \\ge \\left\\lceil \\frac{%s}{4} \\right\\rceil = %s$.\\\\
            Lại có $x_{23} \\ge 0 \\Rightarrow x_1 - 3x_3 \\ge 0 \\Rightarrow 4x_1 - 3x_3 \\ge 3x_1 \\Rightarrow %s \\ge 3x_1 \\Rightarrow x_1 \\le \\left\\lfloor \\frac{%s}{3} \\right\\rfloor = %s$.\\\\
            Kết hợp lại, $x_1 \\in \\left[ %s ; %s \\right]$. Thử trực tiếp ta thấy nghiệm nguyên duy nhất thỏa mãn là $x_1 = %s \\Rightarrow x_3 = %s$.\\\\
            Từ đó suy ra $x_2 = %s - %s = %s$ và $x_{23} = %s - 3 \\cdot %s = %s$.\\\\
            Vậy có %s học sinh ủng hộ một tờ 10.000 đồng và một tờ 20.000 đồng.''' 
                       % (S, m, S, m, S, S+m, S+m, S+m, S+m, S+m, S+m, math.ceil((S+m)/4), S+m, S+m, math.floor((S+m)/3), math.ceil((S+m)/4), math.floor((S+m)/3), a, c, a, c, b, a, c, nbc, nbc))

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            a_s = a + random.choice([-2, -1, 1, 2])
            if a_s <= 0: a_s = a + 2

            th_da_1_d = '\\True Có %s học sinh chỉ ủng hộ một tờ 5.000 đồng' % (a) 
            th_da_1_s = 'Có %s học sinh chỉ ủng hộ một tờ 5.000 đồng' % (a_s) 
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Từ kết quả giải hệ phương trình ở trên, số học sinh chỉ ủng hộ một tờ 5.000 đồng là $x_1 = %s$.''' 
                       %(a))

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            x_val_s = x_val + random.choice([-2, -1, 1, 2])
            if x_val_s <= 0: x_val_s = x_val + 2

            vd_da_1_d = '\\True Nếu gọi số học sinh ủng hộ một tờ 5.000 đồng và một tờ 10.000 đồng là $a$ và số học sinh ủng hộ một tờ 20.000 đồng và một tờ 5.000 đồng là $c$ thì $a+c=%s$' % (x_val) 
            vd_da_1_s = 'Nếu gọi số học sinh ủng hộ một tờ 5.000 đồng và một tờ 10.000 đồng là $a$ và số học sinh ủng hộ một tờ 20.000 đồng và một tờ 5.000 đồng là $c$ thì $a+c=%s$' % (x_val_s) 
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Từ kết quả giải hệ phương trình ở trên, ta có $a+c = x_{12} + x_{13} = x_1 - %s = %s - %s = %s$.'''  
                       %(m, a, m, x_val))

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            b_s = b + random.choice([-2, -1, 1, 2])
            if b_s <= 0: b_s = b + 2

            vdc_da_1_d = '\\True Có %s học sinh lớp 12A chỉ ủng hộ một tờ 10.000 đồng' % (b) 
            vdc_da_1_s = 'Có %s học sinh lớp 12A chỉ ủng hộ một tờ 10.000 đồng' % (b_s) 
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Từ kết quả giải hệ phương trình ở trên, số học sinh lớp 12A chỉ ủng hộ một tờ 10.000 đồng là $x_2 = %s$.'''
                       %(b))

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vdc)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

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

            # Gán lại vào list
            list_nb_1 = [nb_da_1]
            list_th_1 = [th_da_1]
            list_vd_1 = [vd_da_1]
            list_vdc_1 = [vdc_da_1]

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

