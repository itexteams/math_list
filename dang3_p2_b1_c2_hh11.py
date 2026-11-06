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


def bt_dang3_p2_b1_c2_hh11(self):
            # Khai báo biến
            # Khai báo nội dung câu hỏi
            noidungcauhoi = ('''Trong không gian, cho ba đường thẳng phân biệt $a, b, c$.''')

            ########################################################################
            # Nhận biết (Mệnh đề a) ############################################
            # Nội dung: Quan hệ song song và góc
            nb_da_1_d = '\\True Nếu $a // b$ thì $(a, c) = (c, b)$'
            nb_da_1_s = 'Nếu $a // b$ thì $(a, c) \\neq (c, b)$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Theo định nghĩa góc giữa hai đường thẳng trong không gian: Nếu hai đường thẳng $a$ và $b$ song song với nhau thì góc giữa đường thẳng $c$ với đường thẳng $a$ bằng góc giữa đường thẳng $c$ với đường thẳng $b$. Do đó $(a, c) = (c, b)$.''')

            list_nb_2 = [loigiai_nb_1]
            combined_nb = list(zip([nb_da_1], list_nb_2))

            ########################################################################
            # Thông hiểu (Mệnh đề b) ############################################
            # Nội dung: Quan hệ song song và góc (đảo vai trò biến)
            th_da_1_d = '\\True Nếu $c // b$ thì $(a, b) = (a, c)$'
            th_da_1_s = 'Nếu $c // b$ thì $(a, b) < (a, c)$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Tương tự, vì $c // b$ nên góc tạo bởi đường thẳng $a$ với đường thẳng $b$ cũng chính bằng góc tạo bởi đường thẳng $a$ với đường thẳng $c$. Suy ra $(a, b) = (a, c)$.''')

            list_th_2 = [loigiai_th_1]
            combined_th = list(zip([th_da_1], list_th_2))

            ########################################################################
            # Vận dụng (Mệnh đề c) ############################################
            # Nội dung: Hai đường thẳng cùng vuông góc với đường thẳng thứ ba
            vd_da_1_d = 'Nếu $a \\perp c, b \\perp c$ thì $a // b$'
            vd_da_1_s = '\\True Nếu $a \\perp c, b \\perp c$ thì $a$ và $b$ có thể cắt nhau hoặc chéo nhau'
            # Lưu ý: Mệnh đề trong ảnh gốc là "Nếu a vuông c, b vuông c thì a // b" -> Đây là mệnh đề SAI.
            # Để giống ảnh, ta ưu tiên chọn mệnh đề sai để học sinh tích vào cột "Sai".
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Trong không gian, hai đường thẳng cùng vuông góc với một đường thẳng thứ ba thì không nhất thiết song song với nhau. Chúng có thể song song, cắt nhau hoặc chéo nhau. 
                            Ví dụ: Trong hình lập phương, hai cạnh cùng xuất phát từ một đỉnh thì cùng vuông góc với cạnh thứ ba tại đỉnh đó nhưng chúng cắt nhau.''')

            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip([vd_da_1], list_vd_2))

            ########################################################################
            # Vận dụng cao (Mệnh đề d) ############################################
            # Nội dung: Quan hệ vuông góc và góc bất kỳ
            vdc_da_1_d = 'Nếu $a \\perp c$ thì $(a, b) = (c, b)$'
            vdc_da_1_s = '\\True Nếu $a \\perp c$ thì $(a, b)$ và $(c, b)$ không nhất thiết bằng nhau'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Mối quan hệ vuông góc giữa $a$ và $c$ không ảnh hưởng đến góc của chúng với đường thẳng $b$ bất kỳ. Ví dụ, nếu $b$ trùng với $a$ thì $(a, b)=0^\\circ$ còn $(c, b)=90^\\circ$.''')

            list_vdc_2 = [loigiai_vdc_1]
            combined_vdc = list(zip([vdc_da_1], list_vdc_2))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi có từ 1 đến 3 đáp án đúng để đảm bảo tính trắc nghiệm
            while True:
                sel_nb = random.choice(list_nb_da_1)
                sel_th = random.choice(list_th_da_1)
                sel_vd = random.choice(list_vd_da_1)
                sel_vdc = random.choice(list_vdc_da_1)

                if 1 <= count_true_answers([sel_nb, sel_th, sel_vd, sel_vdc]) <= 3:
                    break

            # Gán kết quả cuối cùng
            shuffled_answers = [sel_nb, sel_th, sel_vd, sel_vdc]
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # Xuất nội dung theo mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(shuffled_answers[0]) + '}\n'
                '{' + str(shuffled_answers[1]) + '}\n'
                '{' + str(shuffled_answers[2]) + '}\n'
                '{' + str(shuffled_answers[3]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(shuffled_solutions[0]) + '\n'
                '\\item ' + str(shuffled_solutions[1]) + '\n'
                '\\item ' + str(shuffled_solutions[2]) + '\n'
                '\\item ' + str(shuffled_solutions[3]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

