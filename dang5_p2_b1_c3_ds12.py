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


def bt_dang5_p2_b1_c3_ds12(self):
            # Khai báo biến
            a = randint(3,20)
            a1 =Rational(a,2)

            # Nội dung câu hỏi
            noidungcauhoi = '''Một vật chuyển động với gia tốc $a(t)= %s \\cos t$ (m/$s^2)$.'''%(latex(a))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Tại thời điểm bắt đầu chuyển động, vật có vận tốc bằng $0$. Khi đó, vận tốc của vật được biểu diễn bởi hàm số $v(t)=%s \\sin t$ (m/s)'%(latex(a))
            nb_da_1_s = 'Tại thời điểm bắt đầu chuyển động, vật có vận tốc bằng $0$. Khi đó, vận tốc của vật được biểu diễn bởi hàm số $v(t)=%s \\cos t$ (m/s)'%(latex(a))
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            nb_da_2_d = '\\True Tại thời điểm bắt đầu chuyển động, vật có vận tốc bằng $0$. Khi đó, vận tốc của vật được biểu diễn bởi hàm số $v(t)=%s \\sin t$ (m/s)'%(latex(a))
            nb_da_2_s = 'Tại thời điểm bắt đầu chuyển động, vật có vận tốc bằng $0$. Khi đó, vận tốc của vật được biểu diễn bởi hàm số $v(t)=%s \\cos t$ (m/s)'%(latex(a))
            list_nb_da_2=[nb_da_2_d,nb_da_2_s]

            nb_da_2=random.choice(list_nb_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1, nb_da_2]

            # Nội dung lời giải
            loigiai_nb_1 = ('Ta có $v(t)=\\displaystyle\\int{a(t)\\text{d}t}=\\displaystyle\\int{%s\\cos t\\text{d}t}=%s \\sin t +\\text{C}$. \\\\ \n'
            'Tại thời điểm bắt đầu chuyển động, vật có vận tốc bằng $0$ nên ta có \\\\ \n'
                        '\\hspace*{3cm}$v(0)=%s \\sin 0+\\text{C}=0\\Rightarrow \\text{C}=0$.\\\\ \n'
                        'Vậy $v(t)=%s \\sin t$.'
                            %(latex(a),latex(a),latex(a),latex(a)))
            loigiai_nb_2 = ('Ta có $v(t)=\\displaystyle\\int{a(t)\\text{d}t}=\\displaystyle\\int{%s\\cos t\\text{d}t}=%s \\sin t +\\text{C}$. \\\\ \n'
            'Tại thời điểm bắt đầu chuyển động, vật có vận tốc bằng $0$ nên ta có \\\\ \n'
                        '\\hspace*{3cm}$v(0)=%s \\sin 0+\\text{C}=0\\Rightarrow \\text{C}=0$.\\\\ \n'
                        'Vậy $v(t)=%s \\sin t$.'
                            %(latex(a),latex(a),latex(a),latex(a)))

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1, loigiai_nb_2]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Vận tốc của vật tại thời điểm $\\dfrac{\\pi}{2}$ là $%s$ (m/s)'%(latex(a))
            th_da_1_s = 'Vận tốc của vật tại thời điểm $\\dfrac{\\pi}{2}$ là $%s\\sqrt{3}$ (m/s)'%(latex(a1))
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            th_da_2_d = '\\True Vận tốc của vật tại thời điểm $\\dfrac{\\pi}{6}$ là $%s$ (m/s)'%(latex(a1))
            th_da_2_s = 'Vận tốc của vật tại thời điểm $\\dfrac{\\pi}{6}$ là $%s\\sqrt{3}$ (m/s)'%(latex(a1))
            list_th_da_2=[th_da_2_d,th_da_2_s]

            th_da_2=random.choice(list_th_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1, th_da_2]

            # Nội dung lời giải
            loigiai_th_1 = ('Khi đó vận tốc của vật tại thời điểm $\\dfrac{\\pi}{2}$ là \\\\ \n'
                        '\\hspace*{3cm}$v\\left(\\dfrac{\\pi}{2}\\right)=%s \\sin\\left(\\dfrac{\\pi}{2}\\right)=%s$ (m/s).'
                        %(latex(a),latex(a)))
            loigiai_th_2 = ('Khi đó vận tốc của vật tại thời điểm $\\dfrac{\\pi}{6}$ là \\\\ \n'
                        '\\hspace*{3cm}$v\\left(\\dfrac{\\pi}{6}\\right)=%s \\sin\\left(\\dfrac{\\pi}{6}\\right)=%s$ (m/s).'
                        %(latex(a),latex(a1)))

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1, loigiai_th_2]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Tại thời điểm bắt đầu chuyển động, vật có quãng đường bằng $0$. Khi đó, quãng đường của vật được biểu diễn bởi hàm số $s(t)=-%s \\cos t+%s$ (m)'%(latex(a),latex(a))
            vd_da_1_s = 'Tại thời điểm bắt đầu chuyển động, vật có quãng đường bằng $0$. Khi đó, quãng đường của vật được biểu diễn bởi hàm số $s(t)=%s \\cos t+%s$ (m)'%(latex(a),latex(a))
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            vd_da_2_d = '\\True Tại thời điểm bắt đầu chuyển động, vật có quãng đường bằng $0$. Khi đó, quãng đường của vật được biểu diễn bởi hàm số $s(t)=-%s \\cos t+%s$ (m)'%(latex(a),latex(a))
            vd_da_2_s = 'Tại thời điểm bắt đầu chuyển động, vật có quãng đường bằng $0$. Khi đó, quãng đường của vật được biểu diễn bởi hàm số $s(t)=-%s \\sin t+%s$ (m)'%(latex(a),latex(a))
            list_vd_da_2=[vd_da_2_d,vd_da_2_s]
            vd_da_2=random.choice(list_vd_da_2)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1, vd_da_2]

            # Nội dung lời giải
            loigiai_vd_1 =('Ta có $s(t)=\\displaystyle\\int{v(t)\\text{d}t}=\\displaystyle\\int{%s\\sin t\\text{d}t}=-%s \\cos t +\\text{C}$. \\\\ \n'
            'Tại thời điểm bắt đầu chuyển động, vật có quãng đường bằng $0$ nên ta có \\\\ \n'
                        '\\hspace*{3cm}$s(0)=-%s \\cos 0+\\text{C}=0\\Rightarrow \\text{C}=%s$.'
                        'Vậy $s(t)=-%s \\cos t+%s$ (m).'
                            %(latex(a),latex(a),latex(a),latex(a),latex(a),latex(a)))
            loigiai_vd_2 = ('Ta có $s(t)=\\displaystyle\\int{v(t)\\text{d}t}=\\displaystyle\\int{%s\\sin t\\text{d}t}=-%s \\cos t +\\text{C}$. \\\\ \n'
            'Tại thời điểm bắt đầu chuyển động, vật có quãng đường bằng $0$ nên ta có \\\\ \n'
                        '\\hspace*{3cm}$s(0)=-%s \\cos 0+\\text{C}=0\\Rightarrow \\text{C}=%s$.\\\\ \n'
                        'Vậy $s(t)=-%s \\cos t+%s$ (m).'
                            %(latex(a),latex(a),latex(a),latex(a),latex(a),latex(a)))

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1, loigiai_vd_2]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Quãng đường vật đi được từ thời điểm $t= 0$ (s) đến thời điểm $t=\\pi$ (s) là $%s$ (m)'%(latex(2*a))
            vdc_da_1_s = 'Quãng đường vật đi được từ thời điểm $t= 0$ (s) đến thời điểm $t=\\pi$ (s) là $%s$ (m)'%(latex(a))
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            vdc_da_2_d = '\\True Quãng đường vật đi được từ thời điểm $t= \\dfrac{\\pi}{4} $ (s) đến thời điểm $t=\\dfrac{3\\pi}{4}$ (s) là $%s\\sqrt{2}$ (m)'%(latex(a))
            vdc_da_2_s = 'Quãng đường vật đi được từ thời điểm $t= \\dfrac{\\pi}{4} $ (s) đến thời điểm $t=\\dfrac{3\\pi}{4}$ (s) là $%s\\sqrt{3}$ (m)'%(latex(a))
            list_vdc_da_2=[vdc_da_2_d,vdc_da_2_s]
            vdc_da_2=random.choice(list_vdc_da_2)

            vdc_da_3_d = '\\True Quãng đường vật đi được từ thời điểm $t= \\dfrac{\\pi}{6} $ (s) đến thời điểm $t=\\dfrac{5\\pi}{6}$ (s) là $%s\\sqrt{3}$ (m)'%(latex(a))
            vdc_da_3_s = 'Quãng đường vật đi được từ thời điểm $t= \\dfrac{\\pi}{6} $ (s) đến thời điểm $t=\\dfrac{5\\pi}{6}$ (s) là $%s\\sqrt{2}$ (m)'%(latex(a))
            list_vdc_da_3=[vdc_da_3_d,vdc_da_3_s]
            vdc_da_3=random.choice(list_vdc_da_3)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1, vdc_da_2, vdc_da_3]

            # Nội dung lời giải
            loigiai_vdc_1 = ('Quãng đường vật đi được từ thời điểm $t= 0$ đến thời điểm $t=\\pi$ là\\\\ \n'
                            '\\hspace*{3cm}$s(t)=\\displaystyle\\int\\limits_{0}^{\\pi }{v(t)\\text{d}t}=\\displaystyle\\int\\limits_{0}^{\\pi }{%s\\sin t\\text{d}t}=%s$ (m).'
                            %(latex(a),latex(a*2)))
            loigiai_vdc_2 = ('Quãng đường vật đi được từ thời điểm $t= \\dfrac{\\pi}{4}$ đến thời điểm $t=\\dfrac{3\\pi}{4}$ là\\\\ \n'
                            '\\hspace*{3cm}$s(t)=\\displaystyle\\int\\limits_{\\tfrac{\\pi}{4}}^{\\tfrac{3\\pi}{4}}{v(t)\\text{d}t}=\\displaystyle\\int\\limits_{\\tfrac{\\pi}{4}}^{\\tfrac{3\\pi}{4} }{%s\\sin t\\text{d}t}=%s\\sqrt{2}$ (m).'
                            %(latex(a),latex(a)
                        ))
            loigiai_vdc_3 = ('Quãng đường vật đi được từ thời điểm $t= \\dfrac{\\pi}{6}$ đến thời điểm $t =\\dfrac{5\\pi}{6}$ là\\\\ \n'
                            '\\hspace*{3cm}$s(t)=\\displaystyle\\int\\limits_{\\tfrac{\\pi}{6}}^{\\tfrac{5\\pi}{6}}{v(t)\\text{d}t}=\\displaystyle\\int\\limits_{\\tfrac{\\pi}{6}}^{\\tfrac{5\\pi}{6} }{%s\\sin t\\text{d}t}=%s\\sqrt{3}$ (m).'

                        %(latex(a),latex(a)
                        ))
            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1, loigiai_vdc_2, loigiai_vdc_3]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vdc)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)



            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choiceTFn \n'
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
                '\\end{ex}\n \\end{minipage} \n\n'). replace('\\frac','\\dfrac')
            return content

