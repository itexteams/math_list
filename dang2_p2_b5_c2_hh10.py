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


def bt_dang2_p2_b5_c2_hh10(self):
            # Khai báo biến
            x1=randint(-10,10)
            y1=randint(-10,10)
            x2=randint(-10,10)
            y2=randint(-10,10)
            x3=randint(-10,10)
            y3=randint(-10,10)
            while (x2-x1)*(y3-y1)-(y2-y1)*(x3-x1)==0 or x3-x2==0 or (y3-y2)*(x3-x1)-(y3-y1)*(x3-x2)==0:
                x1=randint(-10,10)
                y1=randint(-10,10)
                x2=randint(-10,10)
                y2=randint(-10,10)
                x3=randint(-10,10)
                y3=randint(-10,10)
            dab=nsimplify(sqrt((x2-x1)**2+(y2-y1)**2))
            dac=nsimplify(sqrt((x3-x1)**2+(y3-y1)**2))
            dbc=nsimplify(sqrt((x3-x2)**2+(y3-y2)**2))
            c=dab+dac+dbc  
            tvh1=(x2-x1)*(x3-x2)+(y2-y1)*(y3-y2)
            tvh2=(x3-x1)*(x3-x2)+(y3-y1)*(y3-y2)
            tvh3=(x2-x1)*(x3-x1)+(y2-y1)*(y3-y1)
            tb=(x1-x2)*(x3-x2)+(y1-y2)*(y3-y2)
            tc=(x1-x3)*(x2-x3)+(y1-y3)*(y2-y3)
            cosa=nsimplify(tvh3/(dab*dac))
            cosb=nsimplify(tb/(dab*dbc))
            cosc=nsimplify(tc/(dbc*dac))
            xm=nsimplify((x1+x2)/2)
            ym=nsimplify((y1+y2)/2)
            xn=nsimplify((x1+x3)/2)
            yn=nsimplify((y1+y3)/2)
            xp=nsimplify((x2+x3)/2)
            yp=nsimplify((y2+y3)/2)
            d1=nsimplify(sqrt((xp-x1)**2+(yp-y1)**2))
            d2=nsimplify(sqrt((xn-x2)**2+(yn-y2)**2))
            d3=nsimplify(sqrt((xm-x3)**2+(ym-y3)**2))

            e=x3-x2
            f=y3-y2
            t=nsimplify((e*(x1-x2)+f*(y1-y2))/(e**2+f**2))
            xh=nsimplify(x2+e*t)
            yh=nsimplify(y2+f*t)

            e1=x3-x1
            f1=y3-y1
            t1=nsimplify((e1*(x2-x1)+f1*(y2-y1))/(e1**2+f1**2))
            xh1=nsimplify(x1+e1*t1)
            yh1=nsimplify(y1+f1*t1)

            e2=x2-x1
            f2=y2-y1
            t2=nsimplify((e2*(x3-x1)+f2*(y3-y1))/(e2**2+f2**2))
            xh2=nsimplify(x1+e2*t2)
            yh2=nsimplify(y1+f2*t2)

            xd=x3+x1-x2
            yd=y3+y1-y2
            m1=x3-x2         
            n1=y3-y2
            p1=x1*(x3-x2)+y1*(y3-y2)
            m2=x3-x1
            n2=y3-y1
            p2=x2*(x3-x1)+y2*(y3-y1)
            y_h=nsimplify((p1*m2-p2*m1)/(n1*m2-n2*m1))
            x_h=nsimplify((p1-n1*y_h)/m1)

            # Nội dung câu hỏi
            noidungcauhoi = '''Trong mặt phẳng tọa độ $Oxy$, cho tam giác $ABC$ với ba điểm $A(%s;%s)$, $B(%s;%s)$ và  $C(%s;%s)$. \n'''%(latex(x1),latex(y1),latex(x2),latex(y2),latex(x3),latex(y3))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Toạ độ vectơ $\\vec{AB}=(%s;%s)$'%(latex(x2-x1),latex(y2-y1))
            nb_da_1_s = 'Toạ độ vectơ $\\vec{AB}=(%s;%s)$'%(latex(-x2+x1),latex(-y2+y1))
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            nb_da_2_d = '\\True Toạ độ vectơ $\\vec{AC}=(%s;%s)$'%(latex(x3-x1),latex(y3-y1))
            nb_da_2_s = 'Toạ độ vectơ $\\vec{AC}=(%s;%s)$'%(latex(-x3+x1),latex(-y3+y1))
            list_nb_da_2=[nb_da_2_d,nb_da_2_s]
            nb_da_2=random.choice(list_nb_da_2)

            nb_da_3_d = '\\True Toạ độ vectơ $\\vec{BC}=(%s;%s)$'%(latex(x3-x2),latex(y3-y2))
            nb_da_3_s = 'Toạ độ vectơ $\\vec{AC}=(%s;%s)$'%(latex(-x3+x2),latex(-y3+y2))
            list_nb_da_3=[nb_da_3_d,nb_da_3_s]
            nb_da_3=random.choice(list_nb_da_3)

            nb_da_4_d = '\\True Toạ độ vectơ $\\vec{BA}=(%s;%s)$'%(latex(-x2+x1),latex(-y2+y1))
            nb_da_4_s = 'Toạ độ vectơ $\\vec{BA}=(%s;%s)$'%(latex(x2-x1),latex(y2-y1))
            list_nb_da_4=[nb_da_4_d,nb_da_4_s]
            nb_da_4=random.choice(list_nb_da_4)

            nb_da_5_d = '\\True Toạ độ vectơ $\\vec{CA}=(%s;%s)$'%(latex(-x3+x1),latex(-y3+y1))
            nb_da_5_s = 'Toạ độ vectơ $\\vec{CA}=(%s;%s)$'%(latex(x3-x1),latex(y3-y1))
            list_nb_da_5=[nb_da_5_d,nb_da_5_s]
            nb_da_5=random.choice(list_nb_da_5)

            nb_da_6_d = '\\True Toạ độ vectơ $\\vec{CB}=(%s;%s)$'%(latex(-x3+x2),latex(-y3+y2))
            nb_da_6_s = 'Toạ độ vectơ $\\vec{CB}=(%s;%s)$'%(latex(x3-x2),latex(y3-y2))
            list_nb_da_6=[nb_da_6_d,nb_da_6_s]
            nb_da_6=random.choice(list_nb_da_6)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1, nb_da_2,nb_da_3,nb_da_4,nb_da_5,nb_da_6]

            # Nội dung lời giải
            loigiai_nb_1 = ('Toạ độ vectơ $\\vec{AB}=(%s;%s)$.'%(latex(x2-x1),latex(y2-y1))
                        )
            loigiai_nb_2 = ('Toạ độ vectơ $\\vec{AC}=(%s;%s)$.'%(latex(x3-x1),latex(y3-y1))
                        )
            loigiai_nb_3 = ('Toạ độ vectơ $\\vec{BC}=(%s;%s)$.'%(latex(x3-x2),latex(y3-y2))
                        )
            loigiai_nb_4 = ('Toạ độ vectơ $\\vec{BA}=(%s;%s)$.'%(latex(-x2+x1),latex(-y2+y1))
                        )
            loigiai_nb_5 = ('Toạ độ vectơ $\\vec{CA}=(%s;%s)$.'%(latex(-x3+x1),latex(-y3+y1))
                        )
            loigiai_nb_6 = ('Toạ độ vectơ $\\vec{CB}=(%s;%s)$.'%(latex(-x3+x2),latex(-y3+y2))
                        )
            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1, loigiai_nb_2,loigiai_nb_3,loigiai_nb_4,loigiai_nb_5,loigiai_nb_6]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Toạ độ trọng tâm của tam giác $ABC$ là $\\left(%s;%s\\right)$'%(latex(nsimplify((x1+x2+x3)/3)),latex(nsimplify((y1+y2+y3)/3)))
            th_da_1_s = 'Toạ độ trọng tâm của tam giác $ABC$ là $\\left(%s;%s\\right)$'%(latex(nsimplify((x1+x2+x3)/3)),latex(nsimplify((-y1-y2-y3)/3)))
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            th_da_2_d = '\\True $\\vec{AB}\\cdot\\vec{BC}=%s$'%(latex(tvh1))
            th_da_2_s = '$\\vec{AB}\\cdot\\vec{BC}=%s$'%(latex(-tvh1))
            list_th_da_2=[th_da_2_d,th_da_2_s]
            th_da_2=random.choice(list_th_da_2)

            th_da_3_d = '\\True $\\vec{AC}\\cdot\\vec{BC}=%s$'%(latex(tvh2))
            th_da_3_s = '$\\vec{AC}\\cdot\\vec{BC}=%s$'%(latex(-tvh2))
            list_th_da_3=[th_da_3_d,th_da_3_s]
            th_da_3=random.choice(list_th_da_3)

            th_da_4_d = '\\True $\\vec{AB}\\cdot\\vec{AC}=%s$'%(latex(tvh3))
            th_da_4_s = '$\\vec{AB}\\cdot\\vec{AC}=%s$'%(latex(-tvh3))
            list_th_da_4=[th_da_4_d,th_da_4_s]
            th_da_4=random.choice(list_th_da_4)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1, th_da_2,th_da_3,th_da_4]

            # Nội dung lời giải
            loigiai_th_1 = ('Gọi $G(x;y)$ là trọng tâm của tam giác $ABC$. \n'
                            'Ta có\\\\ \n'
                            '$\\heva{&x=\\dfrac{%s+%s+%s}{3}\\\\&y=\\dfrac{%s+%s+%s}{3}} \\Leftrightarrow \\heva{&x=%s \\\\ &y=%s}$.\\\\ \n'
                            'Vậy $G(%s;%s)$.'
                            %(latex(x1),latex(x2),latex(x3),latex(y1),latex(y2),latex(y3),latex(nsimplify((x1+x2+x3)/3)),latex(nsimplify((y1+y2+y3)/3)),latex(nsimplify((x1+x2+x3)/3)),latex(nsimplify((y1+y2+y3)/3)))

                        )
            loigiai_th_2 = ('Ta có $\\vec{AB}=(%s;%s)$ và $\\vec{BC}=(%s;%s)$.\\\\ \n'
                            'Suy ra $\\vec{AB}\\cdot\\vec{BC}=%s\\cdot(%s)+%s\\cdot(%s)=%s$.'
                            %(latex(x2-x1),latex(y2-y1),latex(x3-x2),latex(y3-y2),latex(x2-x1),latex(x3-x2),latex(y2-y1),latex(y3-y2),latex(tvh1))
                        )
            loigiai_th_3 = ('Ta có $\\vec{AC}=(%s;%s)$ và $\\vec{BC}=(%s;%s)$.\\\\ \n'
                            'Suy ra $\\vec{AC}\\cdot\\vec{BC}=%s\\cdot(%s)+%s\\cdot(%s)=%s$.'
                            %(latex(x3-x1),latex(y3-y1),latex(x3-x2),latex(y3-y2),latex(x3-x1),latex(x3-x2),latex(y3-y1),latex(y3-y2),latex(tvh2))
                        )
            loigiai_th_4 = ('Ta có $\\vec{AB}=(%s;%s)$ và $\\vec{AC}=(%s;%s)$.\\\\ \n'
                            'Suy ra $\\vec{AB}\\cdot\\vec{AC}=%s\\cdot(%s)+%s\\cdot(%s)=%s$.'
                            %(latex(x2-x1),latex(y2-y1),latex(x3-x1),latex(y3-y1),latex(x2-x1),latex(x3-x1),latex(y2-y1),latex(y3-y1),latex(tvh3))
                        )

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1, loigiai_th_2,loigiai_th_3,loigiai_th_4]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án

            vd_da_1_d = '\\True Chu vi của tam giác $ABC$ bằng $%s$'%(latex(c))
            vd_da_1_s = 'Chu vi của tam giác $ABC$ bằng $%s$'%(latex(2*c))
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            vd_da_2_d = '\\True Độ dài đường trung tuyến kẻ từ đỉnh $A$ của tam giác $ABC$ bằng $%s$'%(latex(d1))
            vd_da_2_s = 'Độ dài đường trung tuyến kẻ từ đỉnh $A$ của tam giác $ABC$ bằng $%s$'%(latex(2*d1))
            list_vd_da_2=[vd_da_2_d,vd_da_2_s]
            vd_da_2=random.choice(list_vd_da_2)

            vd_da_3_d = '\\True Độ dài đường trung tuyến kẻ từ đỉnh $B$ của tam giác $ABC$ bằng $%s$'%(latex(d2))
            vd_da_3_s = 'Độ dài đường trung tuyến kẻ từ đỉnh $B$ của tam giác $ABC$ bằng $%s$'%(latex(2*d2))
            list_vd_da_3=[vd_da_3_d,vd_da_3_s]
            vd_da_3=random.choice(list_vd_da_3)

            vd_da_4_d = '\\True Độ dài đường trung tuyến kẻ từ đỉnh $C$ của tam giác $ABC$ bằng $%s$'%(latex(d3))
            vd_da_4_s = 'Độ dài đường trung tuyến kẻ từ đỉnh $C$ của tam giác $ABC$ bằng $%s$'%(latex(3*d3))
            list_vd_da_4=[vd_da_4_d,vd_da_4_s]
            vd_da_4=random.choice(list_vd_da_4)

            vd_da_5_d = '\\True $\\cos \\widehat{BAC}=%s$'%(latex(cosa))
            vd_da_5_s = '$\\cos \\widehat{BAC}=%s$'%(latex(-cosa))
            list_vd_da_5=[vd_da_5_d,vd_da_5_s]
            vd_da_5=random.choice(list_vd_da_5)

            vd_da_6_d = '\\True $\\cos \\widehat{ABC}=%s$'%(latex(cosb))
            vd_da_6_s = '$\\cos \\widehat{ABC}=%s$'%(latex(-cosb))
            list_vd_da_6=[vd_da_6_d,vd_da_6_s]
            vd_da_6=random.choice(list_vd_da_6)

            vd_da_7_d = '\\True $\\cos \\widehat{ACB}=%s$'%(latex(cosc))
            vd_da_7_s = '$\\cos \\widehat{ACB}=%s$'%(latex(-cosc))
            list_vd_da_7=[vd_da_7_d,vd_da_7_s]
            vd_da_7=random.choice(list_vd_da_7)



            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1, vd_da_2,vd_da_3,vd_da_4,vd_da_5,vd_da_6,vd_da_7]

            # Nội dung lời giải

            loigiai_vd_1 = ('Ta có \\\\ \n'
                            '\\hspace*{1cm} $AB=\\abs{\\vec{AB}}=\\sqrt{(%s-%s)^2+(%s-%s)^2}=%s$\\\\ \n'
                            '\\hspace*{1cm} $AC=\\abs{\\vec{AC}}=\\sqrt{(%s-%s)^2+(%s-%s)^2}=%s$\\\\ \n'
                            '\\hspace*{1cm} $BC=\\abs{\\vec{BC}}=\\sqrt{(%s-%s)^2+(%s-%s)^2}=%s$.\\\\ \n'
                            'Suy ra chu vi tam giác $ABC$ là\\\\ \n'
                            '\\hspace*{1cm} $P_{\\triangle ABC} = AB+AC+BC=%s+%s+%s=%s$.'
                            %(latex(x2),latex(x1),latex(y2),latex(y1),latex(dab),
                            latex(x3),latex(x1),latex(y3),latex(y1),latex(dac),
                            latex(x3),latex(x2),latex(y3),latex(y2),latex(dbc),
                            latex(dab),latex(dac),latex(dbc),latex(c)
                            )
                        )
            loigiai_vd_2 = ('Gọi $M(x;y)$ là trung điểm của $BC$ ta có\\\\ \n'
                            '\\hspace*{1cm} $\\heva{&x=\\dfrac{%s+%s}{2}\\\\&y=\\dfrac{%s+%s}{2}} \\Leftrightarrow \\heva{&x=%s\\\\&y=%s}\\Rightarrow M(%s;%s)$.\\\\ \n'
                            'Suy ra độ dài đường trung tuyến $AM$ là\\\\ \n'
                            '\\hspace*{1cm} $AM=\\abs{\\vec{AM}}=\\sqrt{\\left(%s-%s\\right)^2+\\left(%s-%s\\right)^2}=%s$.'
                            %(latex(x2),latex(x3),latex(y2),latex(y3),latex(xp),latex(yp),latex(xp),latex(yp),
                            latex(xp),latex(x1),latex(yp),latex(y1),latex(d1)
                                )
                        )
            loigiai_vd_3 = ('Gọi $M(x;y)$ là trung điểm của $AC$ ta có\\\\ \n'
                            '\\hspace*{1cm} $\\heva{&x=\\dfrac{%s+%s}{2}\\\\&y=\\dfrac{%s+%s}{2}} \\Leftrightarrow \\heva{&x=%s\\\\&y=%s}\\Rightarrow M(%s;%s)$.\\\\ \n'
                            'Suy ra độ dài đường trung tuyến $BM$ là\\\\ \n'
                            '\\hspace*{1cm} $BM=\\abs{\\vec{BM}}=\\sqrt{\\left(%s-%s\\right)^2+\\left(%s-%s\\right)^2}=%s$.'
                            %(latex(x1),latex(x3),latex(y1),latex(y3),latex(xn),latex(yn),latex(xn),latex(yn),
                            latex(xn),latex(x2),latex(yn),latex(y2),latex(d2)
                                )
                            )
            loigiai_vd_4 = ('Gọi $M(x;y)$ là trung điểm của $AB$ ta có\\\\ \n'
                            '\\hspace*{1cm} $\\heva{&x=\\dfrac{%s+%s}{2}\\\\&y=\\dfrac{%s+%s}{2}} \\Leftrightarrow \\heva{&x=%s\\\\&y=%s}\\Rightarrow M(%s;%s)$.\\\\ \n'
                            'Suy ra độ dài đường trung tuyến $CM$ là\\\\ \n'
                            '\\hspace*{1cm} $CM=\\abs{\\vec{CM}}=\\sqrt{\\left(%s-%s\\right)^2+\\left(%s-%s\\right)^2}=%s$.'
                            %(latex(x1),latex(x2),latex(y1),latex(y2),latex(xm),latex(ym),latex(xm),latex(ym),
                            latex(xm),latex(x3),latex(ym),latex(y3),latex(d3)
                                )
                            )
            loigiai_vd_5 = ('Dễ thấy $\\widehat{BAC}=\\left(\\vec{AB},\\vec{AC}\\right)$.\\\\ \n'
                            'Ta có $\\vec{AB}=(%s;%s)$ và $\\vec{AC}=(%s;%s)$.\\\\ \n'
                            '\\hspace*{1cm} $\\abs{\\vec{AB}}=\\sqrt{(%s)^2+(%s)^2}=%s.$\\\\ \n'
                            '\\hspace*{1cm} $\\abs{\\vec{AC}}=\\sqrt{(%s)^2+(%s)^2}=%s.$\\\\ \n'
                            '\\hspace*{1cm} $\\vec{AB}\\cdot\\vec{AC}=%s\\cdot(%s)+%s\\cdot(%s)=%s$.\\\\ \n'
                            'Suy ra\\\\ \n'
                            '\\hspace*{1cm} $\\cos \\widehat{BAC}=\\cos \\left(\\vec{AB},\\vec{AC}\\right)=\\dfrac{\\vec{AB}\\cdot \\vec{AC}}{\\abs{\\vec{AB}}\\cdot \\abs{\\vec{AC}}}=\\dfrac{%s}{%s\\cdot %s}=%s$.'
                            %(latex(x2-x1),latex(y2-y1),latex(x3-x1),latex(y3-y1),
                            latex(x2-x1),latex(y2-y1),latex(dab),latex(x3-x1),latex(y3-y1),latex(dac),
                            latex(x2-x1),latex(x3-x1),latex(y2-y1),latex(y3-y1),latex(tvh3),
                            latex(tvh3),latex(dab),latex(dac),latex(cosa)
                            )
                        )
            loigiai_vd_6 = ('Dễ thấy $\\widehat{ABC}=\\left(\\vec{BA},\\vec{BC}\\right)$.\\\\ \n'
                            'Ta có $\\vec{BA}=(%s;%s)$ và $\\vec{BC}=(%s;%s)$.\\\\ \n'
                            '\\hspace*{1cm} $\\abs{\\vec{BA}}=\\sqrt{(%s)^2+(%s)^2}=%s.$\\\\ \n'
                            '\\hspace*{1cm} $\\abs{\\vec{BC}}=\\sqrt{(%s)^2+(%s)^2}=%s.$\\\\ \n'
                            '\\hspace*{1cm} $\\vec{BA}\\cdot\\vec{BC}=%s\\cdot(%s)+%s\\cdot(%s)=%s$.\\\\ \n'
                            'Suy ra\\\\ \n'
                            '\\hspace*{1cm} $\\cos \\widehat{ABC}=\\cos \\left(\\vec{BA},\\vec{BC}\\right)=\\dfrac{\\vec{BA}\\cdot \\vec{BC}}{\\abs{\\vec{BA}}\\cdot \\abs{\\vec{BC}}}=\\dfrac{%s}{%s\\cdot %s}=%s$.'
                            %(latex(x1-x2),latex(y1-y2),latex(x3-x2),latex(y3-y2),
                            latex(x1-x2),latex(y1-y2),latex(dab),latex(x3-x2),latex(y3-y2),latex(dbc),
                            latex(x1-x2),latex(x3-x2),latex(y1-y2),latex(y3-y2),latex(tb),
                            latex(tb),latex(dab),latex(dbc),latex(cosb)
                            )
                        )
            loigiai_vd_7 = ('Dễ thấy $\\widehat{ACB}=\\left(\\vec{CA},\\vec{CB}\\right)$.\\\\ \n'
                            'Ta có $\\vec{CA}=(%s;%s)$ và $\\vec{CB}=(%s;%s)$.\\\\ \n'
                            '\\hspace*{1cm} $\\abs{\\vec{CA}}=\\sqrt{(%s)^2+(%s)^2}=%s.$\\\\ \n'
                            '\\hspace*{1cm} $\\abs{\\vec{CB}}=\\sqrt{(%s)^2+(%s)^2}=%s.$\\\\ \n'
                            '\\hspace*{1cm} $\\vec{CA}\\cdot\\vec{CB}=%s\\cdot(%s)+%s\\cdot(%s)=%s$.\\\\ \n'
                            'Suy ra\\\\ \n'
                            '\\hspace*{1cm} $\\cos \\widehat{ACB}=\\cos \\left(\\vec{CA},\\vec{CB}\\right)=\\dfrac{\\vec{CA}\\cdot \\vec{CB}}{\\abs{\\vec{CA}}\\cdot \\abs{\\vec{CB}}}=\\dfrac{%s}{%s\\cdot %s}=%s$.'
                            %(latex(x1-x3),latex(y1-y3),latex(x2-x3),latex(y2-y3),
                            latex(x1-x3),latex(y1-y3),latex(dac),latex(x2-x3),latex(y2-y3),latex(dbc),
                            latex(x1-x3),latex(x2-x3),latex(y1-y3),latex(y2-y3),latex(tc),
                            latex(tc),latex(dac),latex(dbc),latex(cosc)
                            )
                        )


            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1, loigiai_vd_2,loigiai_vd_3,loigiai_vd_4,loigiai_vd_5,loigiai_vd_6,loigiai_vd_7]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án

            vdc_da_1_d = '\\True Với điểm $D(x;y)$ thì tứ giác $ABCD$ là hình bình hành. Giá trị $x+y=%s$'%(latex(xd+yd))
            vdc_da_1_s = 'Với điểm $D(x;y)$ thì tứ giác $ABCD$ là hình bình hành. Giá trị $x+y=%s$'%(latex(xd+yd+2))
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)


            vdc_da_2_d = '\\True Nếu $H(x;y)$ là chân đường cao hạ từ đỉnh $A$ của tam giác $ABC$ thì $x+y=%s$'%(latex(xh+yh))
            vdc_da_2_s = 'Nếu $H(x;y)$ là chân đường cao hạ từ đỉnh $A$ của tam giác $ABC$ thì $x+y=%s$'%(latex(xh-yh))
            list_vdc_da_2=[vdc_da_2_d,vdc_da_2_s]
            vdc_da_2=random.choice(list_vdc_da_2)

            vdc_da_3_d = '\\True Gọi $H(x;y)$ là trực tâm của tam giác $ABC$. Giá trị $x+y=%s$'%(latex(x_h+y_h))
            vdc_da_3_s = 'Gọi $H(x;y)$ là trực tâm của tam giác $ABC$. Giá trị $x+y=%s$'%(latex(x_h+y_h+1))
            list_vdc_da_3=[vdc_da_3_d,vdc_da_3_s]
            vdc_da_3=random.choice(list_vdc_da_3)

            vdc_da_4_d = '\\True Nếu $H(x;y)$ là chân đường cao hạ từ đỉnh $B$ của tam giác $ABC$ thì $x+y=%s$'%(latex(xh1+yh1))
            vdc_da_4_s = 'Nếu $H(x;y)$ là chân đường cao hạ từ đỉnh $B$ của tam giác $ABC$ thì $x+y=%s$'%(latex(xh1-yh1))
            list_vdc_da_4=[vdc_da_4_d,vdc_da_4_s]
            vdc_da_4=random.choice(list_vdc_da_4)

            vdc_da_5_d = '\\True Nếu $H(x;y)$ là chân đường cao hạ từ đỉnh $C$ của tam giác $ABC$ thì $x+y=%s$'%(latex(xh2+yh2))
            vdc_da_5_s = 'Nếu $H(x;y)$ là chân đường cao hạ từ đỉnh $C$ của tam giác $ABC$ thì $x+y=%s$'%(latex(xh2-yh2))
            list_vdc_da_5=[vdc_da_5_d,vdc_da_5_s]
            vdc_da_5=random.choice(list_vdc_da_5)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1, vdc_da_2,vdc_da_3,vdc_da_4,vdc_da_5]

            # Nội dung lời giải

            loigiai_vdc_1 = ('Tứ giác $ABCD$ là hình bình hành khi $\\vec{AD}=\\vec{BC}$.\\\\ \n'
                            'Ta có\\\\ \n'
                            '$\\vec{AD}=(x-%s;y-%s)$ và $\\vec{BC}=(%s;%s)$.\\\\ \n'
                            'Suy ra\\\\ \n'
                            '\\hspace*{1cm} $\\vec{AD}=\\vec{BC} \\Leftrightarrow \\heva{&x-%s=%s\\\\&y-%s=%s} \\Leftrightarrow \\heva{&x=%s\\\\&y=%s} \\Rightarrow D(%s;%s)$.\\\\ \n'
                            'Vậy $x+y=%s+%s=%s$.'
                            %(latex(x1),latex(y1),latex(x3-x2),latex(y3-y2),latex(x1),latex(x3-x2),latex(y1),latex(y3-y2),latex(xd),latex(yd),latex(xd),latex(yd),latex(xd),latex(yd),latex(xd+yd))
                        )

            loigiai_vdc_2 = ('Ta có $\\vec{BH}=(x-%s;y-%s)$ và $\\vec{BC}=(%s;%s)$.\\\\ \n'
                            'Vì 3 điểm $B,H,C$ thẳng hàng nên $\\vec{BH}$ cùng phương với $\\vec{BC}$\\\\ \n'
                            'Suy ra\\\\ \n'
                            '$\\vec{BH}=k\\vec{BC} \\Leftrightarrow \\heva{&x-%s=%sk\\\\&y-%s=%sk} \\Leftrightarrow \\heva{&x=%s+%sk\\\\&y=%s+%sk}$ (1) .\\\\ \n'
                            'Suy ra $H(%s+%sk;%s+%sk)$.\\\\ \n'
                            'Suy ra $\\vec{AH}=(%s+%sk-%s;%s+%sk-%s)=(%s+%sk;%s+%sk)$.\\\\ \n'
                            'Vì $\\vec{AH} \\perp \\vec{BC}$.\\\\ \n'
                            'Suy ra\\\\ \n'
                            '$\\vec{AH} \\cdot \\vec{BC}=0 \\Leftrightarrow (%s+%sk)\\cdot(%s)+(%s+%sk)\\cdot(%s)=0 \\Leftrightarrow k=%s$.\\\\ \n'
                            'Thay $k=%s$ vào (1) ta được\\\\ \n'
                            '\\hspace*{1cm} $\\heva{&x=%s+%s\\cdot \\left(%s\\right)\\\\&y=%s+%s\\cdot \\left(%s\\right)} \\Leftrightarrow \\heva{&x=%s\\\\&y=%s}$.\\\\ \n'
                            'Vậy $x+y=%s+%s=%s$.'
                            %(latex(x2),latex(y2),latex(x3-x2),latex(y3-y2),
                            latex(x2),latex(x3-x2),latex(y2),latex(y3-y2),latex(x2),latex(x3-x2),latex(y2),latex(y3-y2),
                            latex(x2),latex(x3-x2),latex(y2),latex(y3-y2),
                            latex(x2),latex(x3-x2),latex(x1),latex(y2),latex(y3-y2),latex(y1),
                            latex(x2-x1),latex(x3-x2),latex(y2-y1),latex(y3-y2),
                            latex(x2-x1),latex(x3-x2),latex(x3-x2),latex(y2-y1),latex(y3-y2),latex(y3-y2),latex(t),
                            latex(t),
                            latex(x2),latex(x3-x2),latex(t),latex(y2),latex(y3-y2),latex(t),latex(xh),latex(yh),latex(xh),latex(yh),latex(xh+yh))
                            )

            loigiai_vdc_3 =('Vì $H$ là trực tâm của tam giác $ABC$ nên ta có\\\\ \n'
                            '\\hspace*{1cm} $\\heva{&AH \\perp BC\\\\&BH \\perp AC} \\Rightarrow \\heva{&\\vec{AH} \\perp \\vec{BC}\\\\&\\vec{BH} \\perp \\vec{AC}}$.\\\\ \n'
                            'Theo bài ta có\\\\ \n'
                            '\\hspace*{1cm} $\\vec{AH}=(x-%s;y-%s)$.\\\\ \n'
                            '\\hspace*{1cm} $\\vec{BC}=(%s;%s)$.\\\\ \n'
                            '\\hspace*{1cm} $\\vec{BH}=(x-%s;y-%s)$.\\\\ \n'
                            '\\hspace*{1cm} $\\vec{AC}=(%s;%s)$.\\\\ \n'
                            'Ta có hệ phương trình\\\\ \n'
                            '\\begin{eqnarray*} \n'
                            '\\heva{&\\vec{AH} \\cdot \\vec{BC}=0\\\\&\\vec{BH} \\cdot \\vec{AC}=0} &\\Leftrightarrow & \\heva{&(x-%s)\\cdot(%s)+(y-%s)\\cdot(%s)=0\\\\&(x-%s)\\cdot(%s)+(y-%s)\\cdot(%s)=0}\\\\ \n'
                            '&\\Leftrightarrow& \\heva{&%sx+%sy=%s\\\\&%sx+%sy=%s} \\Leftrightarrow \\heva{&x=%s\\\\&y=%s}'
                            '\\end{eqnarray*} \n'
                            'Suy ra $H(%s;%s)$\\\\ \n'
                            'Vậy $x+y=%s+%s=%s$.'
                            %(latex(x1),latex(y1),latex(x3-x2),latex(y3-y2),
                            latex(x2),latex(y2),latex(x3-x1),latex(y3-y1),
                            latex(x1),latex(x3-x2),latex(y1),latex(y3-y2),
                            latex(x2),latex(x3-x1),latex(y2),latex(y3-y1),
                            latex(m1),latex(n1),latex(p1),latex(m2),latex(n2),latex(p2),
                            latex(x_h),latex(y_h),latex(x_h),latex(y_h),latex(x_h),latex(y_h),latex(x_h+y_h)
                            )
                )
            loigiai_vdc_4 = ('Ta có $\\vec{AH}=(x-%s;y-%s)$ và $\\vec{AC}=(%s;%s)$.\\\\ \n'
                            'Vì 3 điểm $A,H,C$ thẳng hàng nên $\\vec{AH}$ cùng phương với $\\vec{AC}$\\\\ \n'
                            'Suy ra\\\\ \n'
                            '$\\vec{AH}=k\\vec{AC} \\Leftrightarrow \\heva{&x-%s=%sk\\\\&y-%s=%sk} \\Leftrightarrow \\heva{&x=%s+%sk\\\\&y=%s+%sk}$ (1) .\\\\ \n'
                            'Suy ra $H(%s+%sk;%s+%sk)$.\\\\ \n'
                            'Suy ra $\\vec{BH}=(%s+%sk-%s;%s+%sk-%s)=(%s+%sk;%s+%sk)$.\\\\ \n'
                            'Vì $\\vec{BH} \\perp \\vec{AC}$.\\\\ \n'
                            'Suy ra\\\\ \n'
                            '$\\vec{BH} \\cdot \\vec{AC}=0 \\Leftrightarrow (%s+%sk)\\cdot(%s)+(%s+%sk)\\cdot(%s)=0 \\Leftrightarrow k=%s$.\\\\ \n'
                            'Thay $k=%s$ vào (1) ta được\\\\ \n'
                            '\\hspace*{1cm} $\\heva{&x=%s+%s\\cdot \\left(%s\\right)\\\\&y=%s+%s\\cdot \\left(%s\\right)} \\Leftrightarrow \\heva{&x=%s\\\\&y=%s}$.\\\\ \n'
                            'Vậy $x+y=%s+%s=%s$.'
                            %(latex(x1),latex(y1),latex(x3-x1),latex(y3-y1),
                            latex(x1),latex(x3-x1),latex(y1),latex(y3-y1),latex(x1),latex(x3-x1),latex(y1),latex(y3-y1),
                            latex(x1),latex(x3-x1),latex(y1),latex(y3-y1),
                            latex(x1),latex(x3-x1),latex(x2),latex(y1),latex(y3-y1),latex(y2),
                            latex(x1-x2),latex(x3-x1),latex(y1-y2),latex(y3-y1),
                            latex(x1-x2),latex(x3-x1),latex(x3-x1),latex(y1-y2),latex(y3-y1),latex(y3-y1),latex(t1),
                            latex(t1),
                            latex(x1),latex(x3-x1),latex(t1),latex(y1),latex(y3-y1),latex(t1),latex(xh1),latex(yh1),latex(xh1),latex(yh1),latex(xh1+yh1))
                            )
            loigiai_vdc_5 = ('Ta có $\\vec{AH}=(x-%s;y-%s)$ và $\\vec{AB}=(%s;%s)$.\\\\ \n'
                            'Vì 3 điểm $A,H,B$ thẳng hàng nên $\\vec{AH}$ cùng phương với $\\vec{AB}$\\\\ \n'
                            'Suy ra\\\\ \n'
                            '$\\vec{AH}=k\\vec{AB} \\Leftrightarrow \\heva{&x-%s=%sk\\\\&y-%s=%sk} \\Leftrightarrow \\heva{&x=%s+%sk\\\\&y=%s+%sk}$ (1) .\\\\ \n'
                            'Suy ra $H(%s+%sk;%s+%sk)$.\\\\ \n'
                            'Suy ra $\\vec{CH}=(%s+%sk-%s;%s+%sk-%s)=(%s+%sk;%s+%sk)$.\\\\ \n'
                            'Vì $\\vec{CH} \\perp \\vec{AB}$.\\\\ \n'
                            'Suy ra\\\\ \n'
                            '$\\vec{CH} \\cdot \\vec{AB}=0 \\Leftrightarrow (%s+%sk)\\cdot(%s)+(%s+%sk)\\cdot(%s)=0 \\Leftrightarrow k=%s$.\\\\ \n'
                            'Thay $k=%s$ vào (1) ta được\\\\ \n'
                            '\\hspace*{1cm} $\\heva{&x=%s+%s\\cdot \\left(%s\\right)\\\\&y=%s+%s\\cdot \\left(%s\\right)} \\Leftrightarrow \\heva{&x=%s\\\\&y=%s}$.\\\\ \n'
                            'Vậy $x+y=%s+%s=%s$.'
                            %(latex(x1),latex(y1),latex(x2-x1),latex(y2-y1),
                            latex(x1),latex(x2-x1),latex(y1),latex(y2-y1),latex(x1),latex(x2-x1),latex(y1),latex(y2-y1),
                            latex(x1),latex(x2-x1),latex(y1),latex(y2-y1),
                            latex(x1),latex(x2-x1),latex(x3),latex(y1),latex(y2-y1),latex(y3),
                            latex(x1-x3),latex(x2-x1),latex(y1-y3),latex(y2-y1),
                            latex(x1-x3),latex(x2-x1),latex(x2-x1),latex(y1-y3),latex(y2-y1),latex(y2-y1),latex(t2),
                            latex(t2),
                            latex(x1),latex(x2-x1),latex(t2),latex(y1),latex(y2-y1),latex(t2),latex(xh2),latex(yh2),latex(xh2),latex(yh2),latex(xh2+yh2))
                            )

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1, loigiai_vdc_2,loigiai_vdc_3,loigiai_vdc_4,loigiai_vdc_5]

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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('--', '+').replace('+-', '-').replace('x-0', 'x').replace('y-0', 'y').replace('x=0-', 'x=-').replace('y=0-', 'y=-').replace('=(0-', '=(-').replace('-1k', '-k').replace('+1k', '+k')
            return content 

