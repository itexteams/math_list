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


def bt_dang1_p2_b2_c3_ds12(self):
            # Khai báo biến
            s0=randint(100,200)
            v0=randint(30,50)
            t0=randint(2,5)
            t1=randint(10,20)
            t2=randint(25,30)
            v01=Rational(v0*1000,3600)
            while s0-t0*Rational(v0*1000,3600)<=v01*t1:
                s0=randint(100,200)
                v0=randint(30,50)
                t0=randint(2,5)
                t1=randint(10,20)
                t2=randint(25,30)
                v01=Rational(v0*1000,3600)
            kq=round(t2*(Rational(s0-t0*Rational(v0*1000,3600)-t1*v01,Rational(t1**2,2)))+v01,1)
            kq1=t2*(Rational(s0-t0*Rational(v0*1000,3600)-t1*v01,Rational(t1**2,2)))+v01
            vkq=round(kq1*3.6,1)
            # Nội dung câu hỏi
            noidungcauhoi = ('Một người điều khiển ô tô đang ở đường dẫn muốn nhập làn vào đường cao tốc. Khi ô tô cách điểm nhập làn $%s$ m, tốc độ của ô tô là $%s$ km/h. $%s$ giây sau đó, ô tô bắt đầu tăng tốc với tốc độ $v(t) = at + b$ ($a, b \\in \\mathbb{R}, a > 0$), trong đó $t$ là thời gian tính bằng giây kể từ khi bắt đầu tăng tốc. Biết rằng ô tô nhập làn cao tốc sau $%s$ giây và duy trì sự tăng tốc trong $%s$ giây kể từ khi bắt đầu tăng tốc. \n'
                            %(latex(s0),latex(v0),latex(t0),latex(t1),latex(t2)
                                ))
            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Quãng đường ô tô đi được từ khi bắt đầu tăng tốc đến khi nhập làn là $%s$ m' %(latex(s0-t0*Rational(v0*1000,3600)))
            nb_da_1_s = 'Quãng đường ô tô đi được từ khi bắt đầu tăng tốc đến khi nhập làn là $%s$ m' %(latex(s0-t0*Rational(v0*1000,3600)-10))
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('Tốc độ ban đầu của ô tô là $%s$ km/h = $%s$ m/s. \\\\ \n'
                            'Quãng đường ô tô đi được trong $%s$ giây đầu tiên là $S_1=%s \\cdot %s =%s$ m. \\\\ \n'
                            'Quãng đường ô tô đi được từ khi bắt đầu tăng tốc đến khi nhập làn là \\\\ \n'
                            '\\hspace*{1cm} $S_2=%s-%s=%s$ m.'
                            %(latex(v0),latex(Rational(v0*1000,3600)),
                            latex(t0),latex(Rational(v0*1000,3600)),latex(t0),latex(t0*Rational(v0*1000,3600)),
                            latex(s0),latex(t0*Rational(v0*1000,3600)),latex(s0-t0*Rational(v0*1000,3600)),
                        ))

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
            th_da_1_d = '\\True Giá trị của $b$ là $%s$' %(latex(v01))
            th_da_1_s = 'Giá trị của $b$ là $%s$' %(latex(v01+1))
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('Ta có $v(t) = at + b$. (m/s). \\\\ \n'
                            'Thời điểm bắt đầu tăng tốc ta có $t = 0, v = %s \\Rightarrow v(0) = b = %s$.'
                            %(latex(v01),latex(v01)
                        ))

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
            vd_da_1_d = '\\True Quãng đường $s(t)$ (đơn vị: mét) mà ô tô đi được trong thời gian $t$ giây ($0 \\leq t \\leq %s$) kể từ khi tăng tốc được tính theo công thức $S(t) = \\int\\limits_0^t v(t) \\text{d}t$' %(latex(t2))
            vd_da_1_s = 'Quãng đường $s(t)$ (đơn vị: mét) mà ô tô đi được trong thời gian $t$ giây ($0 \\leq t \\leq %s$) kể từ khi tăng tốc được tính theo công thức $S(t) = \\int\\limits_{0}^{%s} v(t)\\text{d}t$' %(latex(t2),latex(t2))
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('Do $v(t) > 0$ với $0 \\leq t \\leq %s$, do đó quãng đường $s(t)$ mà ô tô đi được trong thời gian $t$ giây \\\\ ($0 \\leq t \\leq %s$) kể từ khi tăng tốc tính theo công thức: $S(t) = \\int\\limits_0^t v(t)\\text{d}t$. \\\\ \n'
                            'Còn công thức $S(t) = \\int\\limits_{0}^{%s} v(t)\\text{d}t$ là quãng đường ô tô đi được trong $%s$ giây.'
                            %(latex(t2),latex(t2),latex(t2),latex(t2)
                        ))

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
            vdc_da_1_d = '\\True Sau $%s$ giây kể từ khi tăng tốc, tốc độ của ô tô vượt quá tốc độ tối đa cho phép là $%s$ km/h' %(latex(t2),latex(vkq-v01))
            vdc_da_1_s = 'Sau $%s$ giây kể từ khi tăng tốc, tốc độ của ô tô không vượt quá tốc độ tối đa cho phép là $%s$ km/h' %(latex(t2),latex(vkq-v01))
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('Ta có $v(t) = at + %s$. \\\\ \n'
                            'Biết xe nhập làn sau $%s$ giây kể từ lúc tăng tốc, nên \\\\ \n'
                            '\\hspace*{1cm} $%s = \\int\\limits_0^{%s} \\left(at + %s\\right)\\text{d}t '
                            '= \\left( \\frac{at^2}{2} + %st \\right) \\left| \\begin{matrix} %s  \\\\ 0  \\\\  \\end{matrix} \\right. '
                            '= %sa+%s '
                            '\\Rightarrow a = %s$. \\\\ \n '
                            '$\\Rightarrow v(t) = %s t + %s$ (m/s). \\\\ \n'
                            'Tốc độ của ô tô sau $%s$ giây là \\\\ \n'
                            '\\hspace*{1cm} $v(%s) = %s \\cdot %s + %s = %s$ m/s $= %s$ km/h $> %s$ km/h.'
                            %(latex(v01),
                            latex(t1),
                            latex(s0-t0*Rational(v0*1000,3600)),latex(t1),latex(v01),
                            latex(v01),latex(t1),
                            latex(Rational(t1**2,2)),latex(t1*v01), 
                            latex(Rational(s0-t0*Rational(v0*1000,3600)-t1*v01,Rational(t1**2,2))), 
                            latex(Rational(s0-t0*Rational(v0*1000,3600)-t1*v01,Rational(t1**2,2))),latex(v01),
                            latex(t2),latex(t2),latex(t2),latex(Rational(s0-t0*Rational(v0*1000,3600)-t1*v01,Rational(t1**2,2))),latex(v01),
                            latex(kq),latex(vkq),latex(vkq-v01)
                        ))

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1]

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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.0$', '$')
            return content

