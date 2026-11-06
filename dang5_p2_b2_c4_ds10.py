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


def bt_dang5_p2_b2_c4_ds10(self):
            # Khai báo biến
            t=symbols('t')
            k=randint(1,2)
            a=4*k
            b=0.5*k
            c=10*k
            d=1*k
            e=8*k
            hsa=Rational(c*d-a*d-e*b+a*b,d*b**2-b*d**2)
            hsb=Rational(c-a-hsa*b**2,b)
            hsc=a
            f=hsa*t**2+hsb*t+hsc
            lis=[0.1,0.2,0.3]
            t0=random.choice(lis)
            f0=hsa*t0**2+hsb*t0+hsc

            tmax=-Rational(hsb,2*hsa)
            fmax=hsa*tmax**2+hsb*tmax+hsc

            delta=hsb**2-4*hsa*hsc
            t1=(-hsb-sqrt(delta))/(2*hsa)
            t2=(-hsb+sqrt(delta))/(2*hsa)

            t3=round(t1,1)

            # Nội dung câu hỏi
            noidungcauhoi = ('Một vận động viên bóng chuyền đánh một quả bóng lên với vị trí ban đầu từ độ cao $%s$ (m) (tính từ tay đánh bóng đến mặt đất). Tại thời điểm $%s$ giây trái bóng ở độ cao $%s$ (m) và tại $%s$ giây thì trái bóng ở độ cao $%s$ (m).'

                            %(latex(a),latex(b),latex(c),latex(d),latex(e)
                                ))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Công thức tính độ cao của trái bóng là $h(t)=%s$' %(latex(f))
            nb_da_1_s = 'Công thức tính độ cao của trái bóng là $h(t)=%s$' %(latex(f+1))
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('\\immini{'
                            'Dựng hệ trục tọa độ như hình vẽ với gốc tọa độ O trùng với vị trí đánh của vận động viên.\\\\ \n'
                            'Gọi $h(t)=at^2+bt+c$. \\\\ \n'
                            'Vị trí ban đầu là từ độ cao $%s$ (m) nên $A(0;%s)$ thuộc parabol, suy ra $c=%s$. \\\\ \n'
                            'Tại thời điểm $%s$ giây trái bóng ở độ cao $%s$ (m) nên $(%s;%s)$ thuộc parabol, \\\\ \n'
                            'suy ra $%s a+%s b+c=%s$.\\\\ \n'
                            'Tại $%s$ giây trái bóng ở độ cao $%s$ (m) nên $C(%s;%s)$ thuộc parabol, suy ra $%s a+%s b+c=%s$.\\\\ \n'
                            'Ta có hệ phương trình $\\heva{&c=%s \\\\ & %s a+%s b+c=%s \\\\ & %s a+%s b+c=%s} \\Leftrightarrow \\heva{&a=%s \\\\ & b=%s \\\\ &c=%s.}$ \\\\ \n'
                            'Vậy $h(t)=%s$.}{'

                            '''\\definecolor{ffqqqq}{rgb}{1.,0.,0.}
                            \\scalebox{0.6}{ 
            \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
                    \\clip(-1.4672806501968296,-1.3197198532926864) rectangle (2.814316921291328,11.795083518833184);
                    \\draw [samples=50,rotate around={-180.:(0.625,10.25)},xshift=0.625cm,yshift=10.25cm,line width=1.pt ,color=ffqqqq,domain=-1.25:1.25)] plot (\\x,{(\\x)^2/2/0.03125});
                    \\draw [line width=1.pt ,dash pattern=on 4pt off 4pt] (0.,7.997544675532187)-- (0.9999333965545179,8.000799170369483);
                    \\draw [line width=1.pt ,dash pattern=on 4pt off 4pt] (0.9999333965545179,8.000799170369483)-- (1.,0.);
                    \\draw [line width=1.pt ,dash pattern=on 4pt off 4pt] (0.5,0.)-- (0.5,10.);
                    \\draw [line width=1.pt ,dash pattern=on 4pt off 4pt] (0.5,10.)-- (0.,10.);
                    \\draw [->,line width=1.pt ] (-1.,0.) -- (2.5,0.);
                    \\draw [->,line width=1.pt ] (0.,-1.) -- (0.,11.190938526393156);
                    \\draw (-0.7,0.5) node[anchor=north west] {$O$};
                    \\draw (0.037064442488198616,0) node[anchor=north west] {$%s$};
                    \\draw (0.8470964154724446,0) node[anchor=north west] {$%s$};
                    \\draw (-0.54152982392912,4.678374041900176) node[anchor=north west] {$%s$};
                    \\draw (-0.5801027750236079,8.593528577990693) node[anchor=north west] {$%s$};
                    \\draw (-0.8115404815905353,10.541462608262329) node[anchor=north west] {$%s$};
                    \\draw (-0.5801027750236079,11.390067532341062) node[anchor=north west] {$y$};
                    \\draw (1.8499931439291302,0) node[anchor=north west] {$x$};
            \\end{tikzpicture}}'''
                            '}'
                            %(latex(a),latex(a),latex(a),
                            latex(b),latex(c),latex(b),latex(c),
                            latex(b**2),latex(b),latex(c),
                            latex(d),latex(e),latex(d),latex(e),
                            latex(d**2),latex(d),latex(e),
                            latex(a),
                            latex(b**2),latex(b),latex(c),
                            latex(d**2),latex(d),latex(e),
                            latex(hsa),latex(hsb),latex(hsc),
                            latex(f),
                            latex(b),latex(d),latex(a),latex(e),latex(c)
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
            th_da_1_d = '\\True Tại thời điểm $%s$ giây thì trái bóng ở độ cao $%s$ (m) so với mặt đất' %(latex(t0),latex(f0))
            th_da_1_s = 'Tại thời điểm $%s$ giây thì trái bóng ở độ cao $%s$ (m) so với mặt đất' %(latex(t0),latex(f0-1))
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('Với $t=%s$ thì $h(%s)=%s$. \\\\ \n'
                            'Vậy tại thời điểm $%s$ giây thì trái bóng ở độ cao $%s$ (m) so với mặt đất.'
                        %(latex(t0),latex(t0),latex(f0),
                        latex(t0),latex(f0)
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
            vd_da_1_d = '\\True Độ cao lớn nhất của quả bóng so với mặt đất là $%s$' %(latex(fmax))
            vd_da_1_s = 'Độ cao lớn nhất của quả bóng so với mặt đất là $%s$' %(latex(fmax+1))
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('Parabol $h(t)=%s$ có tọa độ đỉnh là $\\left(%s;%s\\right)$.\\\\ \n'
                            'Vậy độ cao lớn nhất của quả bóng so với mặt đất là $%s$.'
                            %(latex(f),latex(tmax),latex(fmax),
                            latex(fmax)
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
            vdc_da_1_d = '\\True Đối phương có khoảng $%s$ giây để cứu bóng trước khi bóng chạm đất' %(latex(t3))
            vdc_da_1_s = 'Đối phương có khoảng $%s$ giây để cứu bóng trước khi bóng chạm đất' %(latex(t3+1))
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('Bóng chạm đất khi $h(t)=0 \\Leftrightarrow %s=0 \\Leftrightarrow \\hoac{& t_1=%s \\\\ & t_2=%s \\,\\, \\text{(loại)}.}$ \\\\ \n'
                            'Vậy đối phương có khoảng $%s$ giây để cứu bóng trước khi bóng chạm đất.'
                    %(latex(f),latex(t1),latex(t2),
                        latex(t3)
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

