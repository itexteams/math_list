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


def bt_dang8_p2_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            a1=randint(1,6)
            a=a1*100
            n1=randint(9,19)
            n=n1/1000
            y1=randint(2000,2020)
            t=randint(3,20)
            k=randint(3,15)
            y2=y1+t
            y3=y1+k
            vd=randint(5,15)
            sd1=a*math.exp(t*n)
            td1=a*n*math.exp(k*n)
            number = Decimal(float(sd1))  # Số cần làm tròn
            sd = number.quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)
            number = Decimal(float(td1))  # Số cần làm tròn
            td = number.quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)


            # Nội dung câu hỏi
            noidungcauhoi = '''Dân số của một quốc gia sau $t$ năm kể từ năm $%s$ được ước tính bởi công thức\\\\ $N(t)=%se^{%st}$ (triệu người)$zz$ \n'''%(latex(y1),latex(a),latex(n))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Dân số của quốc gia đó vào năm $%s$ là $%s$ (triệu người)'%(latex(y2),latex(sd))
            nb_da_1_s = 'Dân số của quốc gia đó vào năm $%s$ là $%s$ (triệu người)'%(latex(y2),latex(sd+2))
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)




            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = (' Vào năm $%s$ ta có $t=%s; N(%s)=%se^{%s\\cdot%s}=%s$$zz$\\\\ \n'
                            'Vậy dân số của quốc gia đó vào năm $%s$ là $%s$ (triệu người)$zz$'%(latex(y2),latex(t),latex(t),latex(a),latex(n),latex(t),latex(sd),latex(y2),latex(sd))
                        )



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
            th_da_1_d = '\\True Đạo hàm của hàm số $N(t)$ là $N\'(t)=%se^{%st}$'%(latex(a*n),latex(n))
            th_da_1_s = 'Đạo hàm của hàm số $N(t)$ là $N\'(t)=%se^{%st}$'%(latex(-a*n),latex(n))
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)



            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('Ta có $N\'(t)=%s\\cdot (%st)\'e^{%st}=%se^{%st}$$zz$'
                            %(latex(a),latex(n),latex(n),latex(a*n),latex(n))
                            )

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

            vd_da_1_d = '\\True Dân số của quốc gia này sẽ tăng trong $%s$ năm tiếp theo (tính từ năm $%s$)'%(latex(vd),latex(y1))
            vd_da_1_s = 'Dân số của quốc gia này sẽ giảm trong $%s$ năm tiếp theo (tính từ năm $%s$)'%(latex(vd),latex(y1))
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1,vd_da_1]

            # Nội dung lời giải

            loigiai_vd_1 = ('Xét hàm số $N(t)=%se^{%st}$ trên đoạn $[0;%s]$$zz$\\\\ \n'
                            'Ta có $N\'(t)=%se^{%st}>0$, $\\forall x \\in [0;%s]$. Suy ra hàm số $N(t)$ đồng biến trên đoạn $[0;%s]$$zz$\\\\ \n'
                            'Vậy dân số của quốc gia này sẽ tăng trong $%s$ năm tiếp theo kể từ năm $%s$$zz$'
                            %(latex(a),latex(n),latex(vd),latex(a*n),latex(n),latex(vd),latex(vd),latex(vd),latex(y1))
                        )

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
            vdc_da_1_d = '\\True Đạo hàm của hàm số $N(t)$ biểu thị tốc độ tăng dân số (tính bằng triệu người/năm)$zz$ Vào năm $%s$ thì tốc độ tăng dân số của quốc gia đó là $%s$ (triệu người/năm)'%(latex(y3),latex(td))
            vdc_da_1_s = 'Đạo hàm của hàm số $N(t)$ biểu thị tốc độ tăng dân số (tính bằng triệu người/năm)$zz$ Vào năm $%s$ thì tốc độ tăng dân số của quốc gia đó là $%s$ (triệu người/năm)'%(latex(y3),latex(td+3))
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)



            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('Vào năm $%s$ thì $t=%s-%s=%s$$zz$\\\\ \n'
                            'Ta có $N\'(t)=%se^{%s t}$$zz$\\\\ \n'
                            'Suy ra tốc độ tăng dân số của quốc gia đó vào năm $%s$ là\\\\ \n' 
                            '$N\'(%s)=%se^{%s\\cdot %s} \\approx %s$ (triệu người/năm)$zz$'
                            %(latex(y3),latex(y3),latex(y1),latex(k),latex(a*n),latex(n),latex(y3),
                            latex(k),latex(a*n),latex(n),latex(k),latex(td))
                        )


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
                '\\end{ex}\n \\end{minipage} \n\n').replace('.',',').replace('$zz$','.').replace(',0e','e')
            return content

